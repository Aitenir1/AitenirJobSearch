from django.urls import path
from . import views

urlpatterns = [
    path(
        route='login',
        view=views.login_page,
        name='login-page',
    ),
    path(
        route='logout',
        view=views.logout_page,
        name='logout-page',
    ),
    path(
        route='register',
        view=views.register,
        name='register'
    )
]

