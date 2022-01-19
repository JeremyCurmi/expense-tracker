from django.urls import path

from . import views

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("<slug:project_slug>", views.project_details, name="detail"),
]
