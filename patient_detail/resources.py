from import_export import resources
from .models import Patient_detail
from .filters import Patient_detail_filter
from import_export.admin import ExportActionMixin




class Patient_detailResource(resources.ModelResource,ExportActionMixin):
    
    class Meta:
        model = Patient_detail
        fields = ('name','age','gender','mobile_number','procedure','reffered_by','date','time')


        