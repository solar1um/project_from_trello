from django.contrib import admin
from posts.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'date_created'
    ]


admin.site.register(Post)
