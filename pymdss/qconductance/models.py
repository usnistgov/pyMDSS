from django.db import models

class search_qconductance(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    serial              = models.CharField(db_column='Serial', max_length=20, null=False, blank=True, help_text='<em>Serial number of the standard</em>')
    #model_no            = models.CharField(db_column='Model', max_length=20, null=False, blank=True, help_text='<em>Model number of the standard</em>')
    #std_manufacturer    = models.CharField(db_column='Standard Manufacturer', max_length=20, null=False, blank=True, help_text='<em>Manufacturer of the standard</em>')
    nominal             = models.CharField(db_column='Nominal', max_length=20, null=True, blank=True, help_text='<em>Nominal standard value in ohms</em>')
    service_id          = models.CharField(db_column='Service Id', max_length=20, null=False, blank=True, help_text='<em>NIST Service Identification</em>')
    process_name        = models.CharField(db_column='Process name', max_length=30, null=False, blank=True, help_text='<em>Name of the process</em>')
    format              = models.CharField(db_column='Format', max_length=10, null=False, blank=True, help_text='<em>Download file format (xlsx if left blank)</em>')

    def __str__(self):
        return self.serial

# Create your models here.
class Quantum_Conductance_Process(models.Model):
    """Magnicon CCC fields

    Args:
        models ([type]): [description]
    """
    nominal                 = models.FloatField(db_column='Nominal (ohm)', blank=True, null=False)
    date                    = models.DateTimeField(db_column='Date', blank=True, null=False)  
    end_time                = models.DateTimeField(db_column='End Time', blank=True, null=False)
    ccc_primary_current     = models.FloatField(db_column='CCC Primary Current', blank=True, null=False)
    cycle_time              = models.FloatField(db_column='Cycle Time', blank=True, null=False)
    ccc_nominal_ratio       = models.CharField(db_column='CCC Nominal Ratio', max_length=16, blank=True, null=False)  
    reference_sn            = models.CharField(db_column='Reference SN', max_length=45, blank=True, null=False)
    serial                  = models.CharField(db_column='Serial', max_length=45, blank=True, null=False)
    c                       = models.FloatField(db_column='C', blank=True, null=False)
    sd_c_field              = models.FloatField(db_column='SD (C)', blank=True, null=False)
    pred_c_field            = models.FloatField(db_column='Pred (C)', blank=True, null=False)
    ccc_r                   = models.FloatField(db_column='CCC R', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meassets                = models.IntegerField(db_column='MeasSets', blank=True, null=False)  # Field name made lowercase.  
    pressure                = models.FloatField(db_column='Pressure', blank=True, null=False)  # Field name made lowercase.    
    ref_temp                = models.FloatField(db_column='Ref Temp', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meas_temp               = models.FloatField(db_column='Unknown Temp', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    c1                      = models.FloatField(db_column='C1', blank=True, null=False)  # Field name made lowercase.
    c2                      = models.FloatField(db_column='C2', blank=True, null=False)  # Field name made lowercase.
    ccc_deltar              = models.FloatField(db_column='CCC deltaR', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sd_c1_field             = models.FloatField(db_column='SD (C1)', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sd_c2_field             = models.FloatField(db_column='SD (C2)', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    samples                 = models.FloatField(db_column='Samples', blank=True, null=False)  # Field name made lowercase.    
    samples_used            = models.FloatField(db_column='Samples Used', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ccc_timing              = models.CharField(db_column='CCC Timing', max_length=45, blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ref_corrected           = models.FloatField(db_column='Ref Corrected', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments                = models.TextField(db_column='Comments', blank=True, null=False)  # Field name made lowercase.
    ref_pcr                 = models.FloatField(db_column='Ref PCR', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ref_tcr                 = models.FloatField(db_column='Ref TCR', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ref_tcr_beta            = models.FloatField(db_column='Ref TCR Beta', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unknown_pcr             = models.FloatField(db_column='Unknown PCR', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unknown_tcr             = models.FloatField(db_column='Unknown TCR', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unknown_tcr_beta        = models.FloatField(db_column='Unknown TCR Beta', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guard                   = models.FloatField(db_column='Guard', blank=True, null=False)  # Field name made lowercase.
    ccc_bvd                 = models.FloatField(db_column='CCC BVD', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ccc_feedback_type       = models.CharField(db_column='CCC Feedback type', max_length=50, blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ccc_feedin              = models.FloatField(db_column='CCC Feedin', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    external_power          = models.CharField(db_column='External Power', max_length=5, blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    room_rh                 = models.FloatField(db_column='Room RH', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magnicon_com_temp       = models.FloatField(db_column='Magnicon com temp', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magnicon_cn_temp        = models.FloatField(db_column='Magnicon cn temp', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magnicon_nv_temp        = models.FloatField(db_column='Magnicon nv temp', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    char_cryostat           = models.FloatField(db_column='Characterization cryostat', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    magnetic_field          = models.FloatField(db_column='Magnetic field', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sample_temperature      = models.FloatField(db_column='Sample temperature', blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    system_id               = models.CharField(db_column='System ID', blank=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_id              = models.CharField(db_column='Service ID', blank=True, max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    process                 = models.CharField(db_column='Process', max_length=100, blank=True, null=False)  # Field name made lowercase.
    area                    = models.CharField(db_column='Area', max_length=20, blank=True, null=False)  # Field name made lowercase.

    def __str__(self):
        return self.process