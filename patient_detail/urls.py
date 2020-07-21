from django.urls import path,include
from .views import detail,detail_list,detailform,export,wholeData
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('',Detail_Form_View.as_view(),name='form'),
    path('detail/',detail,name='detail'),
    path('result/',detail_list,name='result'),
    #path('new/',autocomplete,name='autocomplete')
    path('',detailform,name='form'),
    path('export/',export,name='export'),
    path('wholedata/',wholeData,name="whole")
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)