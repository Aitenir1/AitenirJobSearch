from django.urls import path, include

from books import views


urlpatterns = [
    path(
        route='',
        view=views.books,
        name='books'
    ),
    path(
        route='book-details/<str:pk>',
        view=views.book_details,
        name='book-details'
    ),
    path(
        route='create-book',
        view=views.book_create,
        name='book-create'
    ),
    path(
        route='edit-book/<str:pi>',
        view=views.book_edit,
        name='book-edit'
    ),
    path(
        route='delete-book/<str:pi>',
        view=views.book_delete,
        name='book-delete'
    )

]
