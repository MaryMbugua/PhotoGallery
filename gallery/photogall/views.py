from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Location,Category,Image


# Create your views here.
def landing(request):
    images = Image.get_image_by_id()
    return render(request,'index.html',{"images":images})