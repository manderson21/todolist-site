from django.http import HttpResponseRedirect
from django.shortcuts import render

from main.forms import CreateNewList
from main.models import ToDoList


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
