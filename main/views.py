from django.shortcuts import render

from main.models import ToDoList
from main.forms import CreateNewList


# Create your views here.


def index(response, id_):
    to_do_list = ToDoList.objects.get(id=id_)
    return render(response, "main/list.html", {"to_do_list": to_do_list})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
