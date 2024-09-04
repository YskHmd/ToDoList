from django.shortcuts import render
from django.views.generic.list import ListView
from .models import TodoModel
# Create your views here.

class ToDoList(ListView):
    template_name = 'list.html'
    model = TodoModel