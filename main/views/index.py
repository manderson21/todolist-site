from django.shortcuts import render

from main.models import ToDoList


def index1(response, id_):
    to_do_list = ToDoList.objects.get(id=id_)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in to_do_list.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                to_do_list.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(response, "main/list.html", {"to_do_list": to_do_list})
