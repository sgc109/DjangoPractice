from django.contrib import admin
from .models import *

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

admin.site.register(Bookmark, BookmarkAdmin)
