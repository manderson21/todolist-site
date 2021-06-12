from django.http import HttpResponseRedirect
from django.shortcuts import render

from main.models import ToDoList


def form_create_to_do_list(response):
    if response.method == "POST":
        print(response.POST)
        txt = response.POST.get("txtTodoList")
        if len(txt) > 2:
            todo_list = ToDoList.objects.create(name=response.POST.get("txtTodoList"))
            return HttpResponseRedirect("/%i" % todo_list.id)
    return render(response, "main/create.html")


def form_edit_to_do_list(response, id_):
    to_do_list = ToDoList.objects.get(id=id_)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("btnChangeItem"):
            for item in to_do_list.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("btnNewItem"):
            txt = response.POST.get("txtNewItem")
            if len(txt) > 2:
                to_do_list.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(response, "main/list.html", {"to_do_list": to_do_list})
