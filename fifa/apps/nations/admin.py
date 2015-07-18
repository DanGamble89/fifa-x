from django.contrib import admin

from .models import Nation


@admin.register(Nation)
class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_abbr', 'slug')
