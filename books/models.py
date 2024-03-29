from django.db import models
import uuid


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True, default='default-image.png')
    description = models.TextField(blank=True, null=True, default='It is a new book')
    pub_date = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    # def __repr__(self) -> str:
    #     return self.title


class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
