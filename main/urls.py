from django.urls import path

from main import views

urlpatterns = [
    path('<int:id_>', views.form_edit_to_do_list, name="form_edit_to_do_list"),
    path('', views.home, name="home"),
    path("create/", views.form_create_to_do_list, name="form_creat_to_do_list"),
]