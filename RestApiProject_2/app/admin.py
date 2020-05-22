from django.contrib import admin
from .models import BookNo, Book, BookType, Author


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['published']
    search_fields = ['title', 'description']


admin.site.register(BookNo)
admin.site.register(BookType)
admin.site.register(Author)
