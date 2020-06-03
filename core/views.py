from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead, Contact, StageId, StageContainer

def index(request):
    return render(request, "index.html")

def lead(request, *args, **kwargs):
    progress_width = str(round(100/len(StageId.objects.filter(container=StageContainer.objects.all()[0])),2))
    progress_width = progress_width.replace(",",".")

    data = {
        "items" : Lead.objects.all(),
        "lead_stages" : StageId.objects.filter(container=StageContainer.objects.all()[0]),
        "progress_width" : progress_width
    }
    return render(request, "lead.html", data)
