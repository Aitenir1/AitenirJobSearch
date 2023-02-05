from django.http import HttpResponse
from django.urls import path
from . import views
# Create your views here.
urlpatterns = [
    path('/<int:pk>', views.index),
    path('/all', views.allcourses)
]
