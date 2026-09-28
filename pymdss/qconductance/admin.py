from django.contrib import admin
from .models import QHR_Process

# Register your models here.

@admin.register(QHR_Process)
class QHR_ProcessAdmin(admin.ModelAdmin):
    list_display = ('date', 'serial', 'nominal', 'char_cryostat', 'carrier_density',
                    'sample_temperature', 'magnetic_field', 'service_id')
    list_filter = ('char_cryostat', 'date')
    search_fields = ('serial', 'service_id', 'reference_sn')
    date_hierarchy = 'date'
    ordering = ('-date',)
