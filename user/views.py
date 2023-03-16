from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .Forms import RegisterForm


def login_page(request):
    # request
    if request.user.is_authenticated:
        return redirect('/books')

    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/books')

    return render(
        request=request,
        template_name='login.html'
    )


def logout_page(request):
    logout(request)
    return redirect('/books')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(f"---------------------> {form.is_valid()}")
        if form.is_valid():
            user = form.save()
            print("WE ARE LOGGING IN")
            login(request, user)

            return redirect("books")

    form = RegisterForm()

    return render(
        request=request,
        template_name='registration.html',
        context={"form": form}
    )


