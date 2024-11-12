from django.urls import path
from . import views

app_name = "akimapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="todos"),
]