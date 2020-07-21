from django.urls import path,include
from .views import detail,detail_list,detailform,export,wholeData

urlpatterns = [
    #path('',Detail_Form_View.as_view(),name='form'),
    path('detail/',detail,name='detail'),
    path('result/',detail_list,name='result'),
    #path('new/',autocomplete,name='autocomplete')
    path('',detailform,name='form'),
    path('export/',export,name='export'),
    path('wholedata/',wholeData,name="whole")
    
]