from django.http import HttpResponse
from django.shortcuts import render

courses = [
    {
        "id": 1, 
        "courseName": "Web programming", 
        "department": "Applied Mathematics", 
        "teacher": "Zhavlon Khamidov", 
        "progress": 50,
    },
    {
        "id": 2, 
        "courseName": "Calculus III", 
        "department": "Applied Mathematics", 
        "teacher": "Hussein Chebsi", 
        "progress": 40,
    },
    {
        "id": 3, 
        "courseName": "Russian language II", 
        "department": "Common Courses", 
        "teacher": "Olga Sergeeva", 
        "progress": 60,
    },
    {
        "id": 4, 
        "courseName": "Linear algebra II", 
        "department": "Applied Mathematics", 
        "teacher": "Remudin Mekuria", 
        "progress": 30,
    },
    {
        "id": 5, 
        "courseName": "Introduction to programming", 
        "department": "Applied Mathematics", 
        "teacher": "Zhumaniiaz Mamataliev", 
        "progress": 70,
    },
]

def index(request, pk):
    print(pk, type(pk))
    try: 
        course = [i for i in courses if i["id"] == pk][0]
    except:
        course = None

    print(course)
    return render(request, "main.html", context={"course": course})

def allcourses(request):
    print("hello, world")
    return render(request, 'base.html', context={"courses": courses})