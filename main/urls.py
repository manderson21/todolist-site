from django.urls import path

from main import views

urlpatterns = [
    path('<int:id_>', views.index1, name="index1"),
    path('', views.home, name="home"),
    path("create/", views.create, name="create"),
]