from django.shortcuts import render
from TaskModel.models import Task

# Create your views here.
def show(request):
    data = Task.objects.all()
    return render(request,'show.html',{'data' : data})

def start(request):
    return render(request,'home.html')



