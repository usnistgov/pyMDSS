from django.contrib import admin
from .models import Magnicon_CCC_Process, document, search_standard_resistor, \
                    Scaling_CCC_Process, Thomas_Process
from import_export import resources
                    
class PostMagniconCCC(resources.ModelResource):
    class Meta:
        model = Magnicon_CCC_Process
        fields = '__all__'

# Register your models here.
admin.site.register(Magnicon_CCC_Process)
admin.site.register(Thomas_Process)
admin.site.register(Scaling_CCC_Process)
admin.site.register(document)