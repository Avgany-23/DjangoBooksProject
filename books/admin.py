from django.contrib import admin
from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "read")


admin.site.register(Book, BookAdmin)
