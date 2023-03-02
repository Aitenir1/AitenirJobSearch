from django.shortcuts import render, HttpResponse, redirect
from .models import Book

from .Forms import BookForm


def books(request):
    books = Book.objects.all()

    return render(
        request=request,
        template_name="books.html",
        context={"books": books}
    )


def book_details(request, pk):
    return HttpResponse(f'{pk}')


def book_create(request):
    form = BookForm()

    if request.method == 'POST':
        new_book = BookForm(request.POST)
        print("Bul jak")
        if new_book.is_valid():
            new_book.save()
            return redirect("books")

    return render(
        request=request,
        template_name='book_form.html',
        context={'form': form}
    )


def book_edit(request, pi):
    instance = Book.objects.get(id=pi)
    form = BookForm(instance=instance)

    if request.method == "POST":
        updated_book = BookForm(
            data=request.POST,
            files=request.FILES,
            instance=instance,
        )

        if updated_book.is_valid():
            updated_book.save()
            return redirect("books")

    return render(
        request=request,
        template_name='book_form.html',
        context={'form': form}
    )



def book_delete(request, pi):
    instance = Book.objects.get(id=pi)

    if request.method == "POST":
        instance.delete()

        return redirect("books")

    return render(
        request=request,
        template_name='book-delete.html',
        context={'book': instance}
    )
# def book_delete(request, pi):
#     ins