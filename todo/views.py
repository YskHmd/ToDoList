from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy#url遷移の為
# Create your views here.

class ToDoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class ToDoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
    
class ToDoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel #どこに保存するか指定
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')#url遷移の為
    
class ToDoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel #どこに保存するか指定
    success_url = reverse_lazy('list')#削除後にurl遷移の為
    
class ToDoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel #どこに保存するか指定
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')#編集後にurl遷移の為