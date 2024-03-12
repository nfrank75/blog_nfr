from django.contrib import admin

from .models import Post, Comment, Category


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'intro',
        'body'
    )
    ordering = ('created_at',)
    list_filter = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'name',
        'email',
        'body'
    )
    ordering = ('created_at',)
    list_filter = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
    )
    ordering = ('created_at',)
    list_filter = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
