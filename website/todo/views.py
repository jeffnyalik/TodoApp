# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Todo

from django.shortcuts import render, redirect

def index(request):
    const = Todo.objects.all()
    context = {
        'const': const
    }

    return render(request, 'todo/index.html', context)

def details(request, todo_id):
    todos = Todo.objects.get(id=todo_id)
    context = {
        'todos': todos
    }

    return render(request, 'todo/details.html', context)

    return

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todo')
    else:
        return render(request, 'todo/add.html')
    
        

    
       




