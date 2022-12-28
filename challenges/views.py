from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jan(request):
    return HttpResponse("kanha is a great man")

def feb(request):
    return HttpResponse("Mohit ki shadi")