from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TodoModel
# Create your views here.

class ToDoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class ToDoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel