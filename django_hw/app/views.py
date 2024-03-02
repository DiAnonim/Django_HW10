from django.shortcuts import render
from .models import Todo

def base(request):
    return render(request, 'base.html')

def todo_list(request):
    todos = Todo.objects.exclude(status='D').values_list( "id" ,"title", "status", "deadline")
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, task_id):
    todo = Todo.objects.get(pk=task_id)
    return render(request, 'todo_detail.html', {'todo': todo})