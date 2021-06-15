from django.http import HttpResponseRedirect
from django.shortcuts import render

from todo.models import TodoList


def form_create_todo(response):
    if response.method == "POST":
        print(response.POST)
        txt = response.POST.get("txtTodoList")
        if len(txt) > 2:
            todo_list = TodoList.objects.create(name=response.POST.get("txtTodoList"))
            return HttpResponseRedirect("/app/list/%i" % todo_list.id)
    return render(response, "todo/create.html")


def form_edit_todo(response, id_):
    to_do_list = TodoList.objects.get(id=id_)

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

    return render(response, "todo/list.html", {"to_do_list": to_do_list})
