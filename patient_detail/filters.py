import django_filters
from .models import Patient_detail
from django import forms
from django_filters import DateFromToRangeFilter
from django_filters.widgets import RangeWidget



class Patient_detail_filter(django_filters.FilterSet):
    choise=[
    ("Male","Male"),
    ("Female","Female")
    ]
    
    
    age = django_filters.NumberFilter()
    age__gt = django_filters.NumberFilter(field_name='age', lookup_expr='gt')
    age__lt = django_filters.NumberFilter(field_name='age', lookup_expr='lt')
    gender  = django_filters.ChoiceFilter(label="Gender",choices=choise)

    date = django_filters.DateFilter(
        lookup_expr='icontains',
        widget=forms.DateInput(attrs={'id':'datepicker','type':'text'}))
    date_range = DateFromToRangeFilter(field_name='date',widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD','autocomplete':True}))
    reffered_by = django_filters.CharFilter(lookup_expr='iexact')
    procedure = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Patient_detail
        fields = ['name']
        

        