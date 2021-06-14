from django.urls import path
from django.views.generic import RedirectView

from main import views

urlpatterns = [
    path('', RedirectView.as_view(url="app/")),
    path('app/', RedirectView.as_view(url="list/")),

    # TODO: change home view to be a list
    path('app/list/', views.home, name="home"),
    path('app/list/<int:id_>', views.form_edit_to_do_list, name="form_edit_to_do_list"),

    # TODO: Create today and later views/templates
    # path('app/today/', ),
    # path('app/later/'),

    # TODO: Change create view to a bootstrap modal
    path("app/create/", views.form_create_to_do_list, name="form_creat_to_do_list"),
]