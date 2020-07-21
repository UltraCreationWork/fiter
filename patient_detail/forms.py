from django.forms import ModelForm,Form
from django import forms
from .models import Patient_detail
from .filters import Patient_detail_filter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Field




choise=[
    ("Male","Male"),
    ("Female","Female"),
    ("BOTH","Both")
]
class DetailForm(ModelForm):
    _placeholders = {
        'fieldname': 'fieldname placeholder',
    }
    def __init__(self, *args, **kwargs):
        super(DetailForm, self).__init__(*args, **kwargs)
        helper = self.helper = FormHelper(self)
        layout = helper.layout = Layout()
        helper.form_show_labels = False



        
    
    
    
    class Meta:
        model = Patient_detail
        fields = '__all__'
        widgets = {
            'gender': forms.RadioSelect,
            'name': forms.TextInput(attrs={'placeholder':'Name'}),
            'age': forms.NumberInput(attrs={'placeholder':'Age'}),
            'procedure': forms.TextInput(attrs={'placeholder':'Procedure'}),
            'reffered_by': forms.TextInput(attrs={'placeholder':'Reffered By'}),
            'comment': forms.TextInput(attrs={'placeholder':'Comment'}),
        }



            
        
  

