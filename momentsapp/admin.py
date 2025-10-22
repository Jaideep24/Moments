from django.contrib import admin
from .models import *


@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    ordering = ('-created',)


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'seo', 'created')
    list_filter = ('created',)
    search_fields = ('title', 'description', 'seo')
    ordering = ('-created',)
