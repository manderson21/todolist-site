from django.shortcuts import render
from django.http import HttpResponse
from main.models import ToDoList


# Create your views here.


def index(response, id):
    to_do_list = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"to_do_list":to_do_list})


def home(response):
    return render(response, "main/home.html", {})
