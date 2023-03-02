from django.apps import AppConfig
from django.core.signals import request_finished


def my_callback(sender, **kwargs):
    print("A request was sent")


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'

    def ready(self):
        request_finished.connect(my_callback)

