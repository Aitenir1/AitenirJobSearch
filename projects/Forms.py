from django.forms import ModelForm
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'vote']

