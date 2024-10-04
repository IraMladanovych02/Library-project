from django.contrib import admin

from book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ("title", "author",)
    list_display = ("title", "author", "daily_fee",)
