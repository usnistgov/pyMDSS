from django import forms
from .models import document, Magnicon_CCC_Process, Thomas_Process, search_standard_resistor

class documentation_form(forms.ModelForm):
    class Meta:
        model = document
        fields = ()
        for head in model._meta.get_fields():
            temp = list(fields)
            temp.append(head.name)
            fields = tuple(temp)

class calibration_area_form(forms.ModelForm):
    #mdss_data_file = forms.FileField()
    class Meta:
        model = Magnicon_CCC_Process
        fields = ()
        for head in model._meta.get_fields():
            temp = list(fields)
            temp.append(head.name)
            fields = tuple(temp)
            
class search_standard_resistor_form(forms.ModelForm):
    class Meta:
        model = search_standard_resistor
        fields = '__all__'