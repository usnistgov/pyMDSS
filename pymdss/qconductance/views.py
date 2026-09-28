from django.shortcuts import render
from time import sleep
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import QHR_Process
from .forms import calibration_area_form, search_qconductance_form
from resistors.data_handler import build_search_query, describe_search, read_upload
from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.db import connections
import mysql.connector
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import django.apps
# Save the workbook to a BytesIO buffer
from io import BytesIO
import openpyxl
import datetime
from celery import shared_task
from celery_progress.backend import ProgressRecorder
from django.core.serializers import serialize, deserialize
from celery.result import AsyncResult
from zoneinfo import ZoneInfo
from django.core.cache import cache

import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return render(request, 'qconductance-index.html')

def get_nrows(request):
    key = f"nrows_{request.session.session_key}"
    nrows = cache.get(key, 0)
    return JsonResponse({'nrows': nrows})

def qconductanceCalibrationArea(request):
    return render(request, 'qconductanceCalibrationArea.html')

def calibrationArea(request):
    return render(request, 'calibrationArea.html')

def process(request):
    nrows = request.session.get('nrows', '0')
    return render(request, 'process.html', {'nrows': nrows})
    
def index(request):
    return render(request, 'qconductance-index.html')

def qconductance_upload(request):
    if request.method == 'POST':
        mdss_data_form = calibration_area_form(request.POST, request.FILES)
        if mdss_data_form.is_valid() and request.FILES.getlist('mdss_data_file[]', False) != False:
            # if file is uploaded, then handle the file.
            myfilelist = request.FILES.getlist('mdss_data_file[]')
            task = handle_uploaded_file.apply_async(args=[[files.read() for files in myfilelist], [files.name for files in myfilelist]], ignore_result=False)
            #print('Task status:', task.status)
            mdss_data_form.save(commit = False)
            #context = {'fdata':f_meta}
            context = {'task_id': task.task_id,}
            return render(request, 'qconductance-upload.html', context)
        else:
            return render(request, 'qconductance-upload.html')
    else:
        mdss_data_form = calibration_area_form()
        return render(request, 'qconductance-upload.html')

def get_task_status(request, task_id):
    task = AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Task is still processing...'
        }
    elif task.state == 'SUCCESS':
        response = {
            'state': task.state,
            'result': task.result  # This should be the list returned by the task
        }
    elif task.state == 'FAILURE':
        resffponse = {
            'state': task.state,
            'status': str(task.info)  # The error message if task failed
        }
    return JsonResponse(response)

@shared_task(bind=True, track_started=True)
def handle_uploaded_file(self, encoded_file_data, encoded_file_name):
    msg = []
    error_filenames = []
    uploaded_filenames = []
    already_processed_filenames = []
    db_conn = connections['default']
    cursor = db_conn.cursor()
    progress_recorder = ProgressRecorder(self)
    for ct, file_data in enumerate(encoded_file_data):
        pass_flag = 1  # reset per file, so one bad file doesn't mark the rest as failed
        # First check if the file was uploaded before...
        query  = """SELECT uploaded_filename FROM qconductance_filename WHERE uploaded_filename = "{}" """.format(encoded_file_name[ct])
        cursor.execute(query)
        result = cursor.fetchall()
        num_rows = cursor.rowcount
        #print(result, num_rows)
        if num_rows <= 0:
            # Refuse files with data for another calibration area before saving anything
            mylist, reason = read_upload(file_data, 'quantum conductance')
            if reason:
                print('Error: ', reason)
                pass_flag = 0
            #print('mylist', mylist)
            for data in mylist:
                try:
                    if data != '':
                        data = 'None|' + data
                        i = data.split('|')
                        if i[-1] == '' or i[-1] == '\r' or i[-1] == '\n' or i[-1] =='\r\n':
                            i.pop(-1)
                        if 'QHR Process' in i:
                            # Values map to QHR_Process fields by position, so the
                            # file columns must follow the model's field order.
                            if len(i) == 50:
                                # Old file format, from before carrier density was recorded
                                i.insert(49, None)
                            if len(i) != 51:
                                raise ValueError(f"QHR line has {len(i) - 1} values, expected 49 or 50")
                            if i[49] == '':
                                i[49] = None  # carrier density not measured
                            i[2] = datetime.datetime.strptime(i[2], '%m/%d/%Y %I:%M:%S %p').replace(tzinfo=ZoneInfo("UTC"))
                            try:
                                i[3] = datetime.datetime.strptime(i[3], '%m/%d/%Y %I:%M:%S %p').replace(tzinfo=ZoneInfo("UTC"))
                            except Exception as e:
                                i[3] = datetime.datetime.strptime(i[3], '%m/%d/%Y %I:%M %p').replace(tzinfo=ZoneInfo("UTC"))
                                pass
                            myobj = QHR_Process(*i)
                            myobj.id = None
                            myobj.save()
                except Exception as e:
                    print('Error: ', e)
                    pass_flag = 0
                    reason = str(e)
                    #msg = 'Error processing file: ' + encoded_file_name[ct]
                    #return(msg)
                    break
            if pass_flag:
                # add the filename to the qconductance_filename database
                query = """INSERT INTO qconductance_filename (date_uploaded, uploaded_filename) VALUES (%s, %s)"""
                cursor.execute(query, (datetime.datetime.now().strftime("%d%m%Y_%H%M%S"), encoded_file_name[ct]))
                uploaded_filenames.append(encoded_file_name[ct])
            else:
                error_filenames.append(f"{encoded_file_name[ct]} ({reason})")
        else:
            already_processed_filenames.append(encoded_file_name[ct])       
        progress_recorder.set_progress(int(((ct+1)/len(encoded_file_data))*100), 100)
    for i in uploaded_filenames:
        _msg = " \nSuccessfully uploaded file: " + str(i)
        msg.append(_msg)
    for i in error_filenames:
        _msg = " \nError, cannot upload file: " + str(i)
        msg.append(_msg)
    for i in already_processed_filenames:
        _msg = " \nAlready processed file: " + str(i)
        msg.append(_msg)
    cursor.close()
    #sort_by_date()
    return (msg)

def qconductance_search(request):
    """
    Handle's client request for searching...
    """
    if request.method == 'POST':
        search_data_form = search_qconductance_form(request.POST)
        #for field in search_data_form:
            #print("Field Error:", field.name,  field.errors)
        if search_data_form.is_valid():
            search_data_form.save()
            serial = search_data_form.cleaned_data['serial']
            nominal = search_data_form.cleaned_data['nominal']
            process_name = search_data_form.cleaned_data['process_name']
            format = search_data_form.cleaned_data['format']
            #print(serial, process_name, service_id)
            if serial != '' or nominal != None or process_name != '':
                mydict = {'Serial': serial,
                          'Nominal (ohm)': nominal,
                          'Process': process_name,
                          'Format': format,
                         }
                response = fetch_data(request, mydict)
                if response is None:
                    messages.warning(request, f"No records found for {describe_search(mydict)}.")
                    return render(request, 'qconductance-search.html', {'form': search_data_form})
                return response
            else:
                search_data_form = search_qconductance_form()     
    else:
        # Handle GET request, just render the empty form
        search_data_form = search_qconductance_form()
    return render(request, 'qconductance-search.html', {'form': search_data_form})

def sort_by_date():
    qconductance_tables = get_all_tables()
    #print(qconductance_tables)
    db_conn = connections['default']
    cursor = db_conn.cursor()
    for table in qconductance_tables:
        #print(table)
        if table == 'qconductance_qhr_process':
            query = """SELECT * FROM `{}` ORDER BY STR_TO_DATE(Date, '%m/%d/%Y %h:%i:%S %p') ASC""".format(table)
            try:
                cursor.execute(query)
            except mysql.connector.Error as err:
                print(f"Error: {err}")
    cursor.close()

def get_all_tables():
    query = "SHOW TABLES"
    db_conn = connections['default']
    cursor = db_conn.cursor()
    cursor.execute(query)
    tables = [table[0] for table in cursor.fetchall()]
    cursor.close()
    return(tables)

def fetch_data(request, mydict):
    db_conn = connections['default']
    search_params = list(mydict.values())
    tables = get_all_tables()
    cursor = db_conn.cursor()
    header = []
    results = []
    table_names = []
    nrows = 0
    cache.set(f"nrows_{request.session.session_key}", nrows, timeout=3600)
    for table in tables:
        if  table.startswith('qconductance') and \
            table != ('qconductance_search_qconductance') and \
            table != ('qconductance_filename'):
            cursor.execute(f"DESCRIBE `{table}`")
            columns = [column[0] for column in cursor.fetchall()] # column list of all models
            search_query = build_search_query(table, columns, mydict)
            if search_query is None:
                continue
            # execute the mysql query and fetch the results...
            cursor.execute(*search_query)
            table_results = cursor.fetchall()
            nrows += len(table_results)
            cache.set(f"nrows_{request.session.session_key}", nrows, timeout=3600)
            #print (table_results)
            if table_results != ():
                results.append(table_results)
                table_names.append(table)
                header.append([row[0] for row in cursor.description])
    cursor.close()
    if nrows == 0:
        return None  # nothing found: the search view says so instead of sending an empty file
    #print("rows: ", nrows)
    request.session['nrows'] = str(nrows)
    #export_xlsxwriter(header, results, mydict, table_names)
    if search_params[-1] == 'xlsx':
        response = export_openpyxl(header, results, mydict, table_names)
    elif search_params[-1] == 'text':
        response = export_text(header, results, mydict, table_names)
    else:
        response = export_openpyxl(header, results, mydict, table_names)
    return response
    # Fetch results
    #results = cursor.fetchall()

def fetch_table_data(table_name):
    db_conn = connections['default']
    cursor = db_conn.cursor()
    cursor.execute('select * from ' + table_name)
    header = [row[0] for row in cursor.description]
    rows = cursor.fetchall()
    cursor.close()
    return header, rows

def export_openpyxl(header, rows, mydict, table_names):
    # Create a new Excel workbook
    """
    mydict = {'Serial': serial,
            'Nominal': nominal,
            'Process': process_name,
            'Service ID': service_id,
            }
    """
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    search_params = list(mydict.values())
    serial = search_params[0]
    nominal = search_params[1]
    process = search_params[2]
    service_id = search_params[3]
    not_allowed = ['[', ']', '*', '/', '\\', '?', ':']
    if serial != '' and len(serial) <=31:
        for i in not_allowed:
            if i in serial:
                serial = serial.replace(i, '')
        worksheet.title = str(serial)
    else:
        worksheet.title = "pymdss"
    # Create an new Excel file and add a worksheet.
    if True: #search_params['Format'] == '.csv' or search_params['Format'] == '.xlsx' or search_params['Format'] == '.xls':
        row_index = 1
        column_index = 1
        for head, tables, row in zip(header, table_names, rows):
            #print(head, tables)
            table_string_list= tables.split('_')
            table_string_list.pop(0)
            table_ = ' '.join(table_string_list)
            worksheet.cell(row_index, column_index).value = table_
            row_index += 1
            for column_name in head:
                if column_name != 'id':
                    worksheet.cell(row_index, column_index).value = column_name
                    column_index += 1
            row_index += 1
            column_index = 1
            for r in row:
                for column in r[1:]:
                    worksheet.cell(row_index, column_index).value = column
                    column_index += 1
                row_index += 1
                column_index = 1
        #workbook.save()
        # Save the workbook to a BytesIO buffer
        buffer = BytesIO()
        workbook.save(buffer)
        buffer.seek(0)
        # Create the HttpResponse object with the appropriate MIME type
        response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        # Set content disposition to force browser to download file
        response['Content-Disposition'] = 'attachment; filename="qhr.xlsx"'
    return response 

def export_text(header, rows, mydict, table_names):
    # Create a new Excel workbook
    """
    mydict = {'Serial': serial,
            'Nominal': nominal,
            'Process': process_name,
            'Service ID': service_id,
            }
    """
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    search_params = list(mydict.values())
    serial = search_params[0]
    nominal = search_params[1]
    process = search_params[2]
    service_id = search_params[3]
    if serial != '':
         worksheet.title = str(serial)
    # Create an new Excel file and add a worksheet.
    if True: #search_params['Format'] == '.csv' or search_params['Format'] == '.xlsx' or search_params['Format'] == '.xls':
        row_index = 1
        column_index = 1
        for head, tables, row in zip(header, table_names, rows):
            #print(head, tables)
            worksheet.cell(row_index, column_index).value = tables
            row_index += 1
            for column_name in head:
                worksheet.cell(row_index, column_index).value = column_name
                column_index += 1
            row_index += 1
            column_index = 1
            for r in row:
                for column in r:
                    worksheet.cell(row_index, column_index).value = column
                    column_index += 1
                row_index += 1
                column_index = 1
        #workbook.save()
        # Save the workbook to a BytesIO buffer
        buffer = BytesIO()
        workbook.save(buffer)
        buffer.seek(0)
        # Create the HttpResponse object with the appropriate MIME type
        response = HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        # Set content disposition to force browser to download file
        response['Content-Disposition'] = 'attachment; filename="qhr.txt"'
    return response