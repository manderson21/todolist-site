from django.http import HttpResponseRedirect
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
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
