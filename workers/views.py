from django.shortcuts import render
from . import models


# Create your views here.

def list_workers(request):
    workers_list = models.Worker.objects.order_by('-experience')
    context = {"workers_list": workers_list}
    return render(request, 'index.html', context)
