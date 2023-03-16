import io

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Project, Review


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# class ProjectModel:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description

#
# class ProjectModelSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     description = serializers.CharField()

#
# def encode():
#     model = ProjectModel(
#         title="Napoleon",
#         description="Emperor of the French"
#     )
#
#     model_sr = ProjectModelSerializer(model)
#
#     print(f"{model_sr.data}", sep="\n");
#     # print()
#
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title": "Louis XIV", "description": "King of France"}')
#     data = JSONParser().parse(stream)
#     serializer = ProjectModelSerializer(data=data)
#     serializer.is_valid()
#
#     print(serializer.validated_data)


















