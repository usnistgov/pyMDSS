from django import forms
from .models import document, Magnicon_CCC_Process, Thomas_Process, search_standard_resistor
from django import forms

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
    def __init__(self, *args, **kwargs):
        super(search_standard_resistor_form, self).__init__(*args, **kwargs)
        self.fields['serial'].widget.attrs['class'] = 'form-control'
        self.fields['serial'].label = 'Serial'
        self.fields['serial'].widget.attrs['size'] = 20
    
        self.fields['nominal'].widget.attrs['class'] = 'form-control'
        #self.fields['nominal'].label = 'Nominal'
        #self.fields['nominal'].widget.attrs['size'] = 20
    
        #self.fields['std_manufacturer'].widget.attrs['class'] = 'form-control'
        self.fields['service_id'].widget.attrs['class'] = 'form-control'
        self.fields['process_name'].widget.attrs['class'] = 'form-control'
        self.fields['format'].widget.attrs['class'] = 'form-control'