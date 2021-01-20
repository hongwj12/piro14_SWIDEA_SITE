from django.contrib import admin
from .models import Devtool

# Register your models here.
@admin.register(Devtool)
class DevtoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']