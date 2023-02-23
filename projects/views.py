from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import Project, Review
from .Forms import ProjectForm, ReviewForm
from projects.serializers import ProjectSerializer, ReviewSerializer

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import views


def projects(request):
    all_projects = Project.objects.all()

    return render(
        request=request,
        template_name="test.html",
        context={"projects": all_projects}
    )


def project_detail(request, pi):
    project = Project.objects.get(id=pi)
    reviews = Review.objects.all().filter(project=project)

    review_form = ReviewForm()

    if request.method == "POST":
        new_review_form = ReviewForm(request.POST,)
        new_review = new_review_form.save(commit=False)
        new_review.project = project
        new_review.save()
        return HttpResponseRedirect(request.path_info)

    return render(
        request=request,
        template_name="project-detail.html",
        context={"project": project, "form": review_form, "reviews": reviews}
    )


def project_create(request):
    form = ProjectForm()

    if request.method == "POST":
        project = ProjectForm(request.POST, request.FILES)
        if project.is_valid():
            project.save()
            return redirect("projects")

    return render(
        request=request,
        template_name="project-form.html",
        context={"form": form}
    )


def project_edit(request, pi):
    project = Project.objects.get(id=pi)
    project_form = ProjectForm(
        instance=project
    )

    if request.method == "POST":
        updated_project = ProjectForm(
            data=request.POST,
            files=request.FILES,
            instance=project,
        )

        if updated_project.is_valid():
            updated_project.save()
            return redirect("projects")

    return render(
        request=request,
        template_name="project-edit.html",
        context={"form": project_form}
    )


def project_delete(request, pi):
    if request.method == "POST":
        project = Project.objects.get(id=pi)
        project.delete()

        return redirect("projects")

    return render(
        request=request,
        template_name="project-delete.html",
    )


def review_delete(request, ri):
    review = Review.objects.get(id=ri)
    pi = review.project.id
    review.delete()

    return redirect("project-detail", pi=pi)


def test_template(request):
    return render(
        request=request,
        template_name='test.html',
    )


def create_project(request):
    return render(
        request=request,
        template_name='project-form-2.html',
    )

# class ProjectsApiView(generics.ListAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#
#
# class ReviewApiView(generics.ListAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


class ProjectsApiView(views.APIView):
    def get(self, request):
        return Response({'title': 'Good Work'})

