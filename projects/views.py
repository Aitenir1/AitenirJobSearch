from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Project, Review
from .Forms import ProjectForm, ReviewForm


def projects(request):
    all_projects = Project.objects.all()

    return render(
        request=request,
        template_name="projects.html",
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
        project = ProjectForm(request.POST)
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
        template_name="project-delete.html"
    )


def review_delete(request, ri):
    review = Review.objects.get(id=ri)
    pi = review.project.id
    review.delete()

    return redirect("project-detail", pi=pi)
