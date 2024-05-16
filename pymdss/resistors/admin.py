from django.contrib import admin
from .models import Magnicon_CCC_Process, document,\
                    Scaling_CCC_Process, Thomas_Process, NIST_AAB_Process, \
                    Warshawsky_Process, HR3100_Process, MI_6000B_Process, \
                    MI_6010B_Process, MI_6010C_Process, MI_6010Q_Process, \
                    MI_6010SW_Process, MI_6020Q_Process

# Register your models here.
admin.site.register(Magnicon_CCC_Process)
admin.site.register(Thomas_Process)
admin.site.register(Scaling_CCC_Process)
admin.site.register(document)
admin.site.register(NIST_AAB_Process)
admin.site.register(Warshawsky_Process)
admin.site.register(HR3100_Process)
admin.site.register(MI_6000B_Process)
admin.site.register(MI_6010B_Process)
admin.site.register(MI_6010C_Process)
admin.site.register(MI_6010Q_Process)
admin.site.register(MI_6010SW_Process)
admin.site.register(MI_6020Q_Process)