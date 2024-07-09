from django.contrib import admin
from .models import Book

class MemberAdmin(admin.ModelAdmin):
  list_display = ("id", "bookname", "writername")

# Register your models here.
admin.site.register(Book, MemberAdmin)