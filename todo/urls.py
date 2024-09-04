from django.urls import path
from .views import ToDoList
urlpatterns = [
    path('list/', ToDoList.as_view()),
]
