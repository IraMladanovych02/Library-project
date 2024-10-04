from django.urls import path, include

from rest_framework import routers

from book.views import (
    GenreViewSet,
    AuthorViewSet,
    BookViewSet,
)

app_name = "book"

router = routers.DefaultRouter()

router.register("genres", GenreViewSet)
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)

urlpatterns = [path("", include(router.urls))]