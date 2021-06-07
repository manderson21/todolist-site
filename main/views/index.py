from django.shortcuts import render

from main.models import ToDoList


def index1(response, id_):
    to_do_list = ToDoList.objects.get(id=id_)
    return render(response, "main/list.html", {"to_do_list": to_do_list})
