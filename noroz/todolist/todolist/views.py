from django.shortcuts import render, get_object_or_404
from .models import Todo

def all_todo(request):
    todos = Todo.objects.all()
    return render(request, 'todo/all_todo.html', {'todos': todos})

def todo_detail(request,id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todo/todo_detail.html', {'todo':todo})