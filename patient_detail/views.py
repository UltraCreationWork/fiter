from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from .forms import DetailForm
from django.contrib.messages.views import SuccessMessageMixin
from .models import Patient_detail
from .filters import Patient_detail_filter
import json
from django.http import JsonResponse
from .resources import Patient_detailResource 
from django.http import HttpResponse 
 
         

def detailform(request):
    form = DetailForm(request.POST or request.GET or None)  
    if 'n' in request.GET:
        qs = Patient_detail.objects.filter(name__icontains=request.GET.get('n'))
        names = list()
        for pd in qs:
            names.append(pd.name)
        return JsonResponse(names, safe=False)    
    elif 'p' in request.GET:
        qs = Patient_detail.objects.filter(procedure__icontains=request.GET.get('p'))
        procedure = list()
        for pd in qs:
            procedure.append(pd.procedure)
        return JsonResponse(procedure, safe=False)
    elif 'q' in request.GET:
        rs = Patient_detail.objects.filter(reffered_by__icontains=request.GET.get('q'))
        refs = list()
        for rf in rs:
            refs.append(rf.reffered_by)
        return JsonResponse(refs, safe=False)
    if form.is_valid():
        form.save()
        return redirect('detail/')
    else:
        data = {
            'form':form
        }
        return render(request,'patient_detail/bootform.html',data)



def detail(request):
    data = {
        'details':Patient_detail.objects.all()
    }
    return render(request,'patient_detail/detail.html',data)

data = ''
def detail_list(request):
    if 'n' in request.GET:
        qs = Patient_detail.objects.filter(name__icontains=request.GET.get('n'))
        names = list()
        for pd in qs:
            names.append(pd.name)
        return JsonResponse(names, safe=False)
    elif 'q' in request.GET:
        rs = Patient_detail.objects.filter(reffered_by__icontains=request.GET.get('q'))
        refs = list()
        for rf in rs:
            refs.append(rf.reffered_by)
        return JsonResponse(refs, safe=False)
    elif 'p' in request.GET:
        ps = Patient_detail.objects.filter(procedure__icontains=request.GET.get('p'))
        prs = list()
        for pro in ps:
            prs.append(pro.procedure)
        return JsonResponse(prs, safe=False)
    result = Patient_detail_filter(request.GET, queryset=Patient_detail.objects.all())
    context = {'filter': result}
    global data
    data = result.qs
    return render(request, 'patient_detail/result.html', context)
    
    
def wholeData(request):
    resource = Patient_detailResource()
    dataset = resource.export()
    response = HttpResponse(dataset, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="patient.xls"'
    return response


def export(request):
    
    resource = Patient_detailResource()
    dataset = resource.export(data)
    response = HttpResponse(dataset, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="patient.xls"'
    return response

