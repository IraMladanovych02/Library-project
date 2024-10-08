from django.urls import path

from book.views import BookListView, BookDetailView

app_name = "book"

urlpatterns = [
    path("book/", BookListView.as_view(), name="book-list"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
