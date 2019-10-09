from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': (
            'name',
        )
    }


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': (
            'title',
        )
    }
    list_display = ['id', 'title', 'overview', 'category',
                    'slug', 'is_published', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['is_published', 'category', 'created_at']
    search_fields = ['title', 'overview', 'category__name']


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
