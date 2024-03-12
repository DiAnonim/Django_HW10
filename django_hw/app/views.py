from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Todo
from app.forms import TodoForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

def base(request):
    return render(request, 'base.html')

# def todo_list(request):
#     todos = Todo.objects.exclude(status='D').values_list( "id" ,"title", "status", "deadline")
#     return render(request, 'todo_list.html', {'todos': todos})

# def todo_detail(request, task_id):
#     todo = Todo.objects.get(pk=task_id)
#     return render(request, 'todo_detail.html', {'todo': todo})

class ListTodo(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'

class TodoDetail(DetailView):
    model = Todo
    template_name = 'todo_detail.html'
    context_object_name = 'todo'

class CreateTodo(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'create_todo.html'
    success_url = reverse_lazy('home')

class UpdateTodo(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'update_todo.html'
    success_url = reverse_lazy('home')

class DeleteTodo(DeleteView):
    model = Todo
    template_name = 'delete_todo.html'
    success_url = reverse_lazy('home')
    

