from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead, Contact

def index(request):
    #print(Lead.objects.all()[0].contact.last_name)
    return render(request, "index.html")
