from django.http import HttpResponse
from django.urls import path
from . import views
# Create your views here.
urlpatterns = [
    path(
        route="",
        view=views.projects,
        name="projects",
    ),
    path(
        route="project/<str:pi>", 
        view=views.project_detail, 
        name="project-detail",
    ),
    path(
        route="project-create", 
        view=views.project_create,
        name="project-create",
    ),
    path(
        route="project-edit/<str:pi>",
        view=views.project_edit,
        name="project-edit",
    ),
    path(
        route='project-delete/<str:pi>', 
        view=views.project_delete,
        name="project-delete",
    ),
]
