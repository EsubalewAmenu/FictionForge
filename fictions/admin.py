from django.contrib import admin
from .models import Fiction

@admin.register(Fiction)
class FictionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_date')
    search_fields = ('title', 'author', 'genre')