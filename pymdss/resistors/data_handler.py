from .models import Magnicon_CCC_Process, Thomas_Process, document


def delete_records(mymodel):
    try:
        record = Magnicon_CCC_Process.objects.get(date = '')
        print(record)
        record.delete()
        print("Record deleted successfully!")
    except:
        print("Record doesn't exists")

def build_search_query(table, columns, mydict):
    """
    Returns (query, params) for the filled-in search fields, or None if
    the table is missing one of the searched columns. 'Format' only picks
    the export file type, it is not a column.
    """
    search_terms = {key: val for key, val in mydict.items() if key != 'Format' and val}
    if not all(key in columns for key in search_terms):
        return None
    # A single field is an exact, case-sensitive match; several fields are ANDed with LIKE.
    if len(search_terms) == 1:
        conditions = ["BINARY `{}`=%s".format(key) for key in search_terms]
    else:
        conditions = ["`{}` LIKE %s".format(key) for key in search_terms]
    query = "SELECT * FROM `{}` WHERE ".format(table) + " AND ".join(conditions)
    params = tuple(f"{val}" for val in search_terms.values())
    return query, params

def describe_search(mydict):
    """The filled-in search fields as text, e.g. "Serial 31650, Process MI 6010C Process"."""
    return ', '.join(f"{key} {val}" for key, val in mydict.items() if key != 'Format' and val)

# Processes each calibration area's upload handler stores. Keep in step with the
# 'X Process' branches in resistors/views.py and qconductance/views.py.
UPLOAD_PROCESSES = {
    'standard resistor': ('Magnicon CCC Process', 'Thomas Process', 'Scaling CCC Process',
                          'Warshawsky Process', 'MI 6010C Process', 'MI 6010B Process',
                          'MI 6010SW Process', 'MI 6000B Process', 'MI 6010Q Process',
                          'MI 6020Q Process', 'NIST AAB Process', 'HR3100 Process'),
    'quantum conductance': ('QHR Process',),
}

def read_upload(file_data, area):
    """
    Split an uploaded data file into lines for the upload handler of calibration
    `area`. Returns (lines, reason): reason explains why the file can't be
    uploaded there, in which case lines is empty so nothing gets saved.
    """
    try:
        lines = file_data.decode('utf-8').split('\n')
    except UnicodeDecodeError:
        return [], "it isn't a text data file"
    reason = check_upload_processes(lines, area)
    return ([] if reason else lines), reason

def check_upload_processes(lines, area):
    """
    Return why these lines can't be uploaded in calibration `area`, or None if
    they can. Every line naming a process must belong to the area, and at least
    one must. Lines are matched the same way the upload handlers match them.
    """
    own = UPLOAD_PROCESSES[area]
    found = set()
    has_own = False
    for data in lines:
        if data == '':
            continue
        values = data.split('|')
        if values[-1] in ('', '\r', '\n', '\r\n'):
            values.pop(-1)
        if any(process in values for process in own):
            has_own = True
        else:
            found.update(value for value in values if value.endswith('Process'))
    problems = []
    for process in sorted(found):
        home = next((name for name, processes in UPLOAD_PROCESSES.items() if process in processes), None)
        if home:
            problems.append(f"{process} data, which belongs in the {home} calibration area")
        else:
            problems.append(f"{process} data, which pyMDSS doesn't store")
    if problems:
        return 'it has ' + '; '.join(problems)
    if not has_own:
        return f"it has no {area} data"
    return None
