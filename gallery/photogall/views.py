from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Location,Category,Image


# Create your views here.
def landing(request):
    return render(request,'index.html')