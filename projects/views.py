import os

from django.shortcuts import render, redirect, HttpResponseRedirect

from .models import Project, Review
from .Forms import ProjectForm, ReviewForm
from projects.serializers import ProjectSerializer, ReviewSerializer

from rest_framework import views, generics, viewsets


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
        project = ProjectForm(request.POST, request.FILES)
        if project.is_valid():
            project.save()
            return redirect("projects")

    return render(
        request=request,
        template_name="project-form.html",
        context={"form": form, 'action': 'project-create'}
    )


def project_edit(request, pi):
    project = Project.objects.get(id=pi)
    print("what the fuck is going on here")
    if request.method == "POST":
        updated_project = ProjectForm(
            data=request.POST,
            files=request.FILES,
            instance=project,
        )
        print("Is it working")
        if updated_project.is_valid():
            updated_project.save()
            return redirect("projects")
    else:
        form = ProjectForm(instance=project)

        return render(
            request=request,
            template_name="project-form.html",
            context={"form": form, 'action': 'project-edit'}
        )


def project_delete(request, pi):
    if request.method == "POST":
        project = Project.objects.get(id=pi)

        if project.photo.name != 'default-image.png':
            os.remove(project.photo.path)

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
        template_name='projects.html',
    )


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# class ProjectsApiView(generics.ListAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer#


# class ReviewApiView(generics.ListAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


# class ProjectsAPIList(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer


# class ProjectApiUpdate(generics.UpdateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer


# class ProjectsApiView(views.APIView):
#     def get(self, request):
#         projects_list = Project.objects.all()
#
#         return Response({'projects': ProjectSerializer(projects_list, many=True).data})
#
#     def post(self, request):
#         serializer = ProjectSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # return Response({'post': model_to_dict(project_new)})
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         print(f"------> HEEEEEY {pk}")
#         if not pk:
#             return Response({'error': 'Method put is not allowed'})
#
#         try:
#             instance = Project.objects.get(id=pk)
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         serializer = ProjectSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#
#         if not pk:
#             return Response({'error': 'Method delete is not allowed'})
#
#         try:
#             instance = Project.objects.get(id=pk)
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         instance.delete()
#
#         return Response({'status': 'Ok'})
