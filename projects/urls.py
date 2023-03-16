from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'projects', views.ProjectsViewSet)

# Create your views here.
urlpatterns = [
    path(
        route="",
        view=views.projects,
        name="projects",
    ),
    path(
        route="project-detail/<str:pi>",
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
    # path(
    #     route='test',
    #     view=views.test_template,
    #     name='test-template'
    # ),
    path(
        route='api/v1/',
        view=include(router.urls),
    ),
    # path(
    #     route='api/v1/projects-list/',
    #     view=views.ProjectsViewSet.as_view(
    #         actions={'get': 'list'},
    #     ),
    # ),
    # path(
    #     route='api/v1/projects-list/<str:pk>',
    #     view=views.ProjectsViewSet.as_view(
    #         actions={'put': 'update'}
    #     ),
    # ),
    # path(
    #     route='api/v1/projects-list/',
    #     view=views.ProjectsAPIList.as_view(),
    # ),
    # path(
    #     route='api/v1/projects-list/<str:pk>/',
    #     view=views.ProjectApiUpdate.as_view(),
    # ),
    # path(
    #     route='api/v1/projects-list/<str:pk>/',
    #     view=views.ProjectsApiView.as_view(),
    # ),

]
