from django.contrib import admin
from .models  import Patient_detail
from import_export.admin import ImportExportModelAdmin



class Patient_detail_Admin(ImportExportModelAdmin):
    class Meta:
        fields = ('name','age','gender','mobile_number','procedure','reffered_by','time')


admin.site.register(Patient_detail,Patient_detail_Admin)
   

