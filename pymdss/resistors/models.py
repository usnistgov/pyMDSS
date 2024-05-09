# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table       
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class filename(models.Model):
    date_uploaded = models.CharField(max_length=30, null=False, blank=True)
    uploaded_filename = models.CharField(max_length=50, null=False, blank=True)

    def __str__(self):
        return(self.uploaded_filename)

class document(models.Model):
    """
    [Documentation]

    Args:
        models ([type]): [description]
    """
    filename = models.CharField(db_column='Filename', max_length=100, null=False)
    description = models.TextField(db_column='File Description', null=False, blank=True)

    def __str__(self):
        return self.filename

class search_standard_resistor(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    serial = models.CharField(db_column='Serial', max_length=20, null=False, blank=True)
    model_no = models.CharField(db_column='Model', max_length=20, null=False, blank=True)
    std_manufacturer = models.CharField(db_column='Standard Manufacturer', max_length=20, null=False, blank=True)
    service_id = models.CharField(db_column='Service Id', max_length=20, null=False, blank=True)
    process_name = models.CharField(db_column='Process name', max_length=30, null=False, blank=True)
    format = models.CharField(db_column='Format', max_length=10, null=False, blank=True)

    def __str__(self):
        return self.serial

class Magnicon_CCC_Process(models.Model):
    """Magnicon CCC fields

    Args:
        models ([type]): [description]
    """
    nominal = models.FloatField(db_column='Nominal', blank=True, null=False)
    date = models.CharField(db_column='Date', blank=True, max_length=100)  
    end_time = models.CharField(db_column='End Time', max_length=100, blank=True, null=False)
    ccc_primary_current = models.FloatField(db_column='CCC Primary Current', blank=True, null=False)
    cycle_time = models.FloatField(db_column='Cycle Time', blank=True, null=False)
    ccc_nominal_ratio = models.CharField(db_column='CCC Nominal Ratio', max_length=16, blank=True, null=False)  
# Field name made lowercase. Field renamed to remove unsuitable characters.
    reference_sn = models.CharField(db_column='Reference SN', max_length=45, blank=True, null=False)
    serial = models.CharField(db_column='Serial', max_length=45, blank=True, null=False)
    c = models.FloatField(db_column='C', blank=True, null=False)
    sd_c_field = models.FloatField(db_column='SD (C)', blank=True, null=False)
    pred_c_field = models.FloatField(db_column='Pred (C)', blank=True, null=False)
    ccc_r = models.FloatField(db_column='CCC R', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meassets = models.IntegerField(db_column='MeasSets', blank=True, null=False)  # Field name made lowercase.  
    pressure = models.FloatField(db_column='Pressure', blank=True, null=False)  # Field name made lowercase.    
    ref_temp = models.FloatField(db_column='Ref Temp', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unknown_temp = models.FloatField(db_column='Unknown Temp', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    c1 = models.FloatField(db_column='C1', blank=True, null=False)  # Field name made lowercase.
    c2 = models.FloatField(db_column='C2', blank=True, null=False)  # Field name made lowercase.
    ccc_deltar = models.FloatField(db_column='CCC deltaR', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sd_c1_field = models.FloatField(db_column='SD (C1)', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sd_c2_field = models.FloatField(db_column='SD (C2)', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    samples = models.FloatField(db_column='Samples', blank=True, null=False)  # Field name made lowercase.    
    samples_used = models.FloatField(db_column='Samples Used', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ccc_timing = models.CharField(db_column='CCC Timing', max_length=45, blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ref_corrected = models.FloatField(db_column='Ref Corrected', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments = models.CharField(db_column='Comments', max_length=200, blank=True, null=False)  # Field name made lowercase.
    ref_pcr = models.FloatField(db_column='Ref PCR', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ref_tcr = models.FloatField(db_column='Ref TCR', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ref_tcr_beta = models.FloatField(db_column='Ref TCR Beta', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unknown_pcr = models.FloatField(db_column='Unknown PCR', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unknown_tcr = models.FloatField(db_column='Unknown TCR', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unknown_tcr_beta = models.FloatField(db_column='Unknown TCR Beta', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guard = models.FloatField(db_column='Guard', blank=True, null=False)  # Field name made lowercase.
    ccc_bvd = models.FloatField(db_column='CCC BVD', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ccc_feedback_type = models.CharField(db_column='CCC Feedback type', blank=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ccc_feedin = models.FloatField(db_column='CCC Feedin', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    external_power = models.CharField(db_column='External Power', max_length=5, blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    room_rh = models.FloatField(db_column='Room RH', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magnicon_com_temp = models.FloatField(db_column='Magnicon com temp', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magnicon_cn_temp = models.FloatField(db_column='Magnicon cn temp', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magnicon_nv_temp = models.FloatField(db_column='Magnicon nv temp', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    system_id = models.CharField(db_column='System ID', blank=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_id = models.CharField(db_column='Service ID', blank=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    process = models.CharField(db_column='Process', max_length=100, blank=True, null=False)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=20, blank=True, null=False)  # Field name made lowercase.

    def __str__(self):
        return self.process

class Thomas_Process(models.Model):
    nominal = models.FloatField(db_column='Nominal', blank=True, null=False)
    comments = models.CharField(db_column='Comments', max_length=200, blank=True, null=False)
    date = models.CharField(db_column='Date', blank=True, max_length=100)
    meas_voltage = models.FloatField(db_column='Meas Voltage', blank=True, null=False)
    dummy = models.FloatField(db_column='Dummy', blank=True, null=False)
    meas_position = models.FloatField(db_column='Meas Position', blank=True, null=False)
    serial = models.CharField(db_column='Serial', max_length=20, blank=True, null=False)
    meas_function = models.CharField(db_column='Meas Function', max_length=5, blank=True, null=False)
    c = models.FloatField(db_column='C', blank=True, null=False)
    sd_c_field = models.FloatField(db_column='SD (C)', blank=True, null=False)
    pred_c_field = models.FloatField(db_column='Pred (C)', blank=True, null=False)
    unknown_temp = models.FloatField(db_column='Meas Temp', blank=True, null=False)
    room_rh = models.FloatField(db_column='RH', blank=True, null=False)
    pressure = models.FloatField(db_column='Pressure', blank=True, null=False)
    sense_avg = models.FloatField(db_column='Sens Avg', blank=True, null=False)
    sensitivity = models.FloatField(db_column='Sensitivity', blank=True, null=False)
    oil_depth = models.FloatField(db_column='Oil Depth', blank=True, null=False)
    c_pred = models.FloatField(db_column='C-Pred', blank=True, null=False)
    range = models.FloatField(db_column='Range', blank=True, null=False)
    ref_tcr = models.FloatField(db_column='TCR Corr', blank=True, null=False)
    ref_pcr = models.FloatField(db_column='PCR Corr', blank=True, null=False)
    system_id = models.CharField(db_column='System ID', blank=True, max_length=100)
    service_id = models.CharField(db_column='Service ID', blank=True, max_length=20)
    process = models.CharField(db_column='Process', max_length=100, blank=True, null=False)
    area = models.CharField(db_column='Area', max_length=20, blank=True, null=False)
    
    def __str__(self):
        return self.process
 																					
class Scaling_CCC_Process(models.Model):
    nominal = models.FloatField(db_column='Nominal', blank=True, null=False)
    system_id = models.CharField(db_column='System ID', max_length=10, blank=True, null=False)
    date = models.CharField(db_column='Date', blank=True, max_length=100)
    ccc_primary_current = models.FloatField(db_column='CCC Primary Current', blank=True, null=False)
    meas_delay = models.FloatField(db_column='Meas Delay', blank=True, null=False)
    ccc_nom_ratio = models.CharField(db_column='CCC Nom Ratio', max_length=10, blank=True, null=False)
    comments = models.CharField(db_column='Comments', max_length=200, blank=True, null=False)
    serial = models.CharField(db_column='Serial', max_length=20, blank=True, null=False)
    c = models.FloatField(db_column='C', blank=True, null=False)
    sd_c_field = models.FloatField(db_column='SD (C)', blank=True, null=False)
    pred_c_field = models.FloatField(db_column='Pred (C)', blank=True, null=False)
    reference_sn = models.CharField(db_column='Reference SN', max_length=45, blank=True, null=False)
    ccc_r = models.FloatField(db_column='CCC R', blank=True, null=False)
    meassets = models.IntegerField(db_column='MeasSets', blank=True, null=False)
    pressure = models.FloatField(db_column='Pressure', blank=True, null=False)
    unknown_temp = models.FloatField(db_column='Meas Temp', blank=True, null=False)
    unknown_temp_2 = models.FloatField(db_column='Meas Temp 2', blank=True, null=False)
    dvm_nplc = models.FloatField(db_column='DVM NPLC', blank=True, null=False)
    dvm_readings = models.IntegerField(db_column='DVM readings', blank=True, null=False)
    ccc_timing = models.CharField(db_column='CCC Timing', max_length=45, blank=True, null=False)
    service_id = models.CharField(db_column='Service ID', blank=True, max_length=20)
    process = models.CharField(db_column='Process', max_length=100, blank=True, null=False)
    area = models.CharField(db_column='Area', max_length=20, blank=True, null=False)
    
    def __str__(self):
        return self.process
    
class Warshawsky_Process(models.Model):
    nominal = models.FloatField(db_column='Nominal', blank=True, null=False)
    comments = models.CharField(db_column='Comments', max_length=200, blank=True, null=False)
    date = models.CharField(db_column='Date', blank=True, max_length=100)
    meas_voltage = models.FloatField(db_column='Meas Voltage', blank=True, null=False)
    dummy = models.FloatField(db_column='Dummy', blank=True, null=False)
    meas_position = models.FloatField(db_column='Meas Position', blank=True, null=False)
    serial = models.CharField(db_column='Serial', max_length=20, blank=True, null=False)
    meas_function = models.CharField(db_column='Meas Function', max_length=5, blank=True, null=False)
    c = models.FloatField(db_column='C', blank=True, null=False)
    sd_c_field = models.FloatField(db_column='SD (C)', blank=True, null=False)
    pred_c_field = models.FloatField(db_column='Pred (C)', blank=True, null=False)
    unknown_temp = models.FloatField(db_column='Meas Temp', blank=True, null=False)
    room_rh = models.FloatField(db_column='RH', blank=True, null=False)
    pressure = models.FloatField(db_column='Pressure', blank=True, null=False)
    sense_avg = models.FloatField(db_column='Sens Avg', blank=True, null=False)
    sensitivity = models.FloatField(db_column='Sensitivity', blank=True, null=False)
    guard = models.FloatField(db_column='Guard', blank=True, null=False)
    c_pred = models.FloatField(db_column='C-Pred', blank=True, null=False)
    range = models.FloatField(db_column='Range', blank=True, null=False)
    ref_tcr = models.FloatField(db_column='TCR Corr', blank=True, null=False)
    ref_pcr = models.FloatField(db_column='PCR Corr', blank=True, null=False)
    system_id = models.CharField(db_column='System ID', blank=True, max_length=100)
    service_id = models.CharField(db_column='Service ID', blank=True, max_length=20)
    process = models.CharField(db_column='Process', max_length=100, blank=True, null=False)
    area = models.CharField(db_column='Area', max_length=20, blank=True, null=False)
    
    def __str__(self):
        return self.process
"""
class MI_6010C_Process(models.Model):
    nominal = models.FloatField(db_column='Nominal (ohm)', blank=True, null=False)
    date = models.CharField(db_column='Date', blank=True, max_length=100)
    end_time = models.CharField(db_column='End Time', max_length=100, blank=True, null=False)
    meas_current = models.FloatField(db_column='Meas Current (A)', blank=True, null=False)
    meas_delay = models.FloatField(db_column='Meas Delay (s)', blank=True, null=False)
    meas_temp = models.FloatField(db_column='Meas Temp (C)', blank=True, null=False)
    reference_sn = models.CharField(db_column='Reference SN', max_length=45, blank=True, null=False)
    serial = models.CharField(db_column='Serial', max_length=20, blank=True, null=False)
    ratio = models.FloatField(db_column='Ratio', blank=True, null=False)
    sd_c_field = models.FloatField(db_column='SD (C) (ppm)', blank=True, null=False)
    mi_stats = models.CharField(db_column='MI Stats', max_length=20, blank=True, null=False)
    r = models.FloatField(db_column=' R (ohm)', blank=True, null=False)
    system_id = models.CharField(db_column='System ID', max_length=10, blank=True, null=False)
    comments = models.TextField(db_column='Comments', blank=True, null=False)
    mi_range = models.CharField(db_column='MI Range', max_length=50, blank=True, null=False)
    mi_channels = models.CharField(db_column='MI Channels', max_length=50, blank=True, null=False)
    mi_components = models.CharField(db_column='MI Components', max_length=100, blank=True, null=False)
    service_id = models.CharField(db_column='Service ID', blank=True, max_length=20)
    process = models.CharField(db_column='Process', max_length=100, blank=True, null=False)
    area = models.CharField(db_column='Area', max_length=20, blank=True, null=False)

    def __str__(self):
        return self.process

class MI_6010B_Process(models.Model):
    nominal = models.FloatField(db_column='Nominal (ohm)', blank=True, null=False)
    date = models.CharField(db_column='Date', blank=True, max_length=100)
    end_time = models.CharField(db_column='End Time', max_length=100, blank=True, null=False)
    meas_current = models.FloatField(db_column='Meas Current (A)', blank=True, null=False)
    meas_delay = models.FloatField(db_column='Meas Delay (s)', blank=True, null=False)
    meas_temp = models.FloatField(db_column='Meas Temp (C)', blank=True, null=False)
    reference_sn = models.CharField(db_column='Reference SN', max_length=45, blank=True, null=False)
    serial = models.CharField(db_column='Serial', max_length=20, blank=True, null=False)
    ratio = models.FloatField(db_column='Ratio', blank=True, null=False)
    sd_c_field = models.FloatField(db_column='SD (C) (ppm)', blank=True, null=False)
    mi_stats = models.CharField(db_column='MI Stats', max_length=20, blank=True, null=False)
    r = models.FloatField(db_column=' R (ohm)', blank=True, null=False)
    system_id = models.CharField(db_column='System ID', max_length=10, blank=True, null=False)
    comments = models.TextField(db_column='Comments', blank=True, null=False)
    mi_range = models.CharField(db_column='MI Range', max_length=50, blank=True, null=False)
    mi_channels = models.CharField(db_column='MI Channels', max_length=50, blank=True, null=False)
    mi_components = models.CharField(db_column='MI Components', max_length=100, blank=True, null=False)
    service_id = models.CharField(db_column='Service ID', blank=True, max_length=20)
    process = models.CharField(db_column='Process', max_length=100, blank=True, null=False)
    area = models.CharField(db_column='Area', max_length=20, blank=True, null=False)

    def __str__(self):
        return self.process
"""