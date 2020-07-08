from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
from todoapp.models import todo
from django.http import HttpResponseRedirect

def index(request):
    todo_items=todo.objects.all().order_by("-added_date")
    return render(request, 'todoapp/index.html',{"todo_items":todo_items})


# .create helps in updating th database
# here a dictionary is created with content as key , and the dictionary is request.POST
def add_todo(request):
    current_date=timezone.now()
    content=request.POST["content"]
    created_obj=todo.objects.create(added_date=current_date,text=content) 
    return HttpResponseRedirect('/')



def delete_todo(request,todo_id):
    todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
