from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<str:pk>/',views.updateTask,name="update_task"),
    path('deletetask/<int:todo_id>/',views.deleteTask,name="delete_task"),
    # the <int:todo_id> catches the integer comeing from form and stores it in the todo_id parameter
    
]
