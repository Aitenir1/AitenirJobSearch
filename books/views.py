from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author, Publisher

from .Forms import BookForm, AuthorForm, PublisherForm


schema = {
    'book': [Book, BookForm],
    'author': [Author, AuthorForm],
    'publisher': [Publisher, PublisherForm],
}


# def books(request):
#     book_list = Book.objects.all()
#
#     return render(
#         request=request,
#         template_name="books.html",
#         context={"books": book_list}
#     )


def items(request, cl=None):
    if cl is None:
        cl = 'book'

    model = schema[cl][0]

    items_list = model.objects.all()

    return render(
        request=request,
        template_name=f'{cl}s.html',
        context={f'{cl}s_list': items_list}
    )


def create(request, cl):
    model = schema[cl][0]
    form = schema[cl][1]()

    if request.method == 'POST':

        new_ent = schema[cl][1](request.POST)
        print(new_ent.is_valid())
        if new_ent.is_valid():
            new_ent.save()

            return redirect("items", cl=cl)

    return render(
        request=request,
        template_name='form.html',
        context={
            'cl': cl,
            'form': form,
            'action': f'create'}
    )


def edit(request, cl, mi):
    model = schema[cl][0]
    instance = model.objects.get(id=mi)
    form = schema[cl][1](instance=instance)

    if request.method == 'POST':
        print('------------------> Great 2')

        updated_ent = schema[cl][1](request.POST, instance=instance)
        print(updated_ent.is_valid())
        if updated_ent.is_valid():
            print("Here is the problem")
            updated_ent.save()

            return redirect("items", cl=cl)

    return render(
        request=request,
        template_name='form.html',
        context={
            'cl': cl,
            'form': form,
            'action': 'edit'}
    )


def delete(request, cl, mi):
    model = schema[cl][0]
    instance = model.objects.get(id=mi)

    if request.method == 'POST':
        instance.delete()

        return redirect("items", cl=cl )

    return render(
        request=request,
        template_name='delete.html',
        context={
            'cl': cl,
            'entity': instance,
        }
    )

# def book_create(request):
#     form = BookForm()
#
#     if request.method == 'POST':
#         new_book = BookForm(request.POST)
#         if new_book.is_valid():
#             new_book.save()
#             return redirect("books")
#
#     return render(
#         request=request,
#         template_name='book-form.html',
#         context={'form': form, 'action': 'book-create'}
#     )


# def book_edit(request, pi):
#     instance = Book.objects.get(id=pi)
#     form = BookForm(instance=instance)
#
#     if request.method == "POST":
#         updated_book = BookForm(
#             data=request.POST,
#             instance=instance,
#         )
#
#         if updated_book.is_valid():
#             updated_book.save()
#             return redirect("books")
#
#     return render(
#         request=request,
#         template_name='book-form.html',
#         context={'form': form, 'action': 'edit'}
#     )


# def book_delete(request, pi):
#     instance = Book.objects.get(id=pi)
#
#     if request.method == "POST":
#         instance.delete()
#
#         return redirect("books")
#
#     return render(
#         request=request,
#         template_name='book-delete.html',
#         context={'book': instance}
#     )


# Authors
# def authors(request):
#     authors_list = Author.objects.all()
#     #
#     return render(
#         request=request,
#         template_name='authors.html',
#         context={
#             'authors_list': authors_list
#         }
#     )

#
# def author_create(request):
#     form = AuthorForm()
#
#     if request.method == 'POST':
#         new_author = AuthorForm(request.POST)
#
#         if new_author.is_valid():
#             new_author.save()
#
#             return redirect('authors-list')
#
#     return render(
#         request=request,
#         template_name='author-form.html',
#         context={'form': form, 'action': 'create'}
#     )

#
# def author_edit(request, pi):
#     instance = Author.objects.get(id=pi)
#
#     form = AuthorForm(instance=instance)
#
#     if request.method == 'POST':
#         updated_author = AuthorForm(request.POST, instance=instance)
#
#         if updated_author.is_valid():
#             updated_author.save()
#
#             return redirect('authors-list')
#
#     return render(
#         request=request,
#         template_name='author-form.html',
#         context={'form': form, 'action': 'edit'}
#     )

#
# def author_delete(request, ai):
#     instance = Author.objects.get(id=ai)
#
#     if request.method == 'POST':
#         instance.delete()
#
#         return redirect('authors-list')
#
#     return render(
#         request=request,
#         template_name='author-delete.html',
#         context={'author': instance}
#     )


# Publishers
# def publishers(request):
#     publishers_list = Publisher.objects.all()
#     #
#     return render(
#         request=request,
#         template_name='publishers.html',
#         context={
#             'publishers_list': publishers_list
#         }
#     )

#
# def publisher_create(request):
#     form = PublisherForm()
#
#     if request.method == 'POST':
#         new_publisher = PublisherForm(request.POST)
#
#         if new_publisher.is_valid():
#             new_publisher.save()
#
#             return redirect('publisher-list')
#
#     return render(
#         request=request,
#         template_name='publisher-form.html',
#         context={'form': form, 'action': 'create'}
#     )


# def publisher_edit(request, pi):
#     instance = Publisher.objects.get(id=pi)
#
#     form = PublisherForm(instance=instance)
#
#     if request.method == 'POST':
#         updated_publisher = PublisherForm(request.POST, instance=instance)
#
#         if updated_publisher.is_valid():
#             updated_publisher.save()
#
#             return redirect('publisher-list')
#
#     return render(
#         request=request,
#         template_name='publisher-form.html',
#         context={'form': form, 'action': 'edit'}
#     )


# def publisher_delete(request, ai):
#     instance = Publisher.objects.get(id=ai)
#
#     if request.method == 'POST':
#         instance.delete()
#
#         return redirect('publishers-list')
#
#     return render(
#         request=request,
#         template_name='publisher-delete.html',
#         context={'publisher': instance}
#     )