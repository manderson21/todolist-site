from django.shortcuts import render
from django.http import HttpResponse
from main.models import ToDoList


# Create your views here.


def index(response, id):
    to_do_list = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {})


def home(response):
    return render(response, "main/home.html", {})
