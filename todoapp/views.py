from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
from todoapp.models import todo
from django.http import HttpResponseRedirect
from .forms import *


def index(request):
    todo_items = todo.objects.all().order_by("-added_date")
    form = todoappform()
    if request.method == 'POST':
        form = todoappform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {"todo_items": todo_items, 'form': form}
    return render(request, 'todoapp/index.html', context)


def updateTask(request, pk):
    task = todo.objects.get(id=pk)
    form = todoappform(instance=task)
    if request.method=="POST":
        form = todoappform(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'todoapp/update.html',context)

def deleteTask(request,todo_id):
    todo.objects.get(id=todo_id).delete()
    return redirect('/')
