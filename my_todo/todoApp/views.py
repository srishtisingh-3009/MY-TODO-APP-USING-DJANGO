from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks= Task.objects.all()
    form=TaskForm()
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'tasks':tasks,'form':form}
    return render(request,'todoApp/first.html',context)
def updateTask(request,pk):
    task1=Task.objects.get(id=pk)
    form=TaskForm(instance=task1)
    if request.method =='POST':
        form=TaskForm(request.POST,instance=task1)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'form':form}
    return render(request,'todoApp/update_task.html',context)
def deleteTask(request,pk):
    item=Task.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect('/')
    context={'item':item}
    return render(request,'todoApp/delete.html',context)
