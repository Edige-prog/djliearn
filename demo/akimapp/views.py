from django.shortcuts import render, HttpResponse
from .models import TodoItem

def home(request):
    return render(request, "home.html", {"name": "Akim"})

def todos(request):
    return render(request, "todos.html", {"todos": TodoItem.objects.all()})

