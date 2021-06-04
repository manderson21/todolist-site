from django.shortcuts import render
from django.http import HttpResponse
from main.models import ToDoList


# Create your views here.


def index(response, id):
    to_do_list = ToDoList.objects.get(id=id)
    item = to_do_list.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1></br><p>%s</p>" % (to_do_list.name, item.text))
