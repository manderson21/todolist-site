from django.urls import path
from django.views.generic import RedirectView, TemplateView

from todo import views

urlpatterns = [
    path('', RedirectView.as_view(url="app/")),
    path('app/', RedirectView.as_view(url="list/")),

    # TODO: change home view to be a list
    path('app/list/', TemplateView.as_view(template_name="todo/base.html")),
    path('app/list/<int:id_>', views.form_edit_todo, name="form_edit_to_do_list"),

    # TODO: Create today and later views/templates
    # path('app/today/', ),
    # path('app/later/'),

    # TODO: Change create view to a bootstrap modal
    path("app/create/", views.form_create_todo, name="form_create_to_do_list"),
]