from django.contrib import admin
from .models import Idea

# Register your models here.
@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ['title']