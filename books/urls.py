from django.urls import path, include

from books import views


urlpatterns = [
    path(
        route='',
        view=views.items,
        name='books'
    ),

    # path(
    #     route='books-list/',
    #     view=views.books,
    #     name='books-list'
    # ),

    path(
        route='create/<str:cl>',
        view=views.create,
        name='create'
    ),

    path(
        route='edit/<str:cl>/<str:mi>',
        view=views.edit,
        name='edit'
    ),

    path(
        route='delete/<str:cl>/<str:mi>',
        view=views.delete,
        name='delete'
    ),

    path(
        '<str:cl>',
        view=views.items,
        name='items'
    ),

    # path(
    #     route='book-create',
    #     view=views.book_create,
    #     name='book-create'
    # ),
    # path(
    #     route='book-edit/<str:pi>',
    #     view=views.book_edit,
    #     name='book-edit'
    # ),
    # path(
    #     route='book-delete/<str:pi>',
    #     view=views.book_delete,
    #     name='book-delete'
    # ),
    # path(
    #     route='authors-list',
    #     view=views.authors,
    #     name='authors-list'
    # ),
    # path(
    #     route='author-create',
    #     view=views.author_create,
    #     name='author-create'
    # ),
    # path(
    #     route='author-edit/<str:pi>',
    #     view=views.author_edit,
    #     name='author-edit',
    # ),
    # path(
    #     route='author-delete/<str:ai>',
    #     view=views.author_delete,
    #     name='author-delete'
    # ),
    # path(
    #     route='publishers-list',
    #     view=views.publishers,
    #     name='publishers-list'
    # ),
    # path(
    #     route='publisher-create',
    #     view=views.publisher_create,
    #     name='publisher-create'
    # ),
    # path(
    #     route='publisher-edit/<str:pi>',
    #     view=views.publisher_edit,
    #     name='publisher-edit',
    # ),
    # path(
    #     route='publisher-delete/<str:ai>',
    #     view=views.publisher_delete,
    #     name='publisher-delete'
    # ),

]
