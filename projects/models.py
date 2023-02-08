from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self) -> str:
        return self.title