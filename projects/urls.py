from django.http import HttpResponse
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

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
    path(
        route='review-delete/<str:ri>',
        view=views.review_delete,
        name='review-delete',
    ),
    path(
        route='test',
        view=views.test_template,
        name='test-template'
    ),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
