from django.shortcuts import render


def home(response):
    return render(response, "todo/index.html", {})
