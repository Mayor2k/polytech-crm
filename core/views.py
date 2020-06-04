from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def lead(request, *args, **kwargs):
    progress_width = str(round(100/len(StageId.objects.filter(_container=StageContainer.objects.all()[0])),2))
    progress_width = progress_width.replace(",",".")

    data = {
        "items" : Lead.objects.all(),
        "lead_stages" : StageId.objects.filter(_container=StageContainer.objects.all()[0]),
        "progress_width" : progress_width
    }
    return render(request, "lead.html", data)

def deal(request):
    progress_width = str(round(100/len(StageId.objects.filter(_container=StageContainer.objects.all()[1])),2))
    progress_width = progress_width.replace(",",".")

    data = {
        "items" : Deal.objects.all(),
        "deal_stages" : StageId.objects.filter(_container=StageContainer.objects.all()[1]),
        "progress_width" : progress_width
    }
    return render(request, "deal.html", data)

def contact(request):
    data = {
        "items" : Contact.objects.all(),
    }
    return render(request, "contact.html", data)

def company(request):
    data = {
        "items" : Company.objects.all(),
    }
    return render(request, "company.html", data)
