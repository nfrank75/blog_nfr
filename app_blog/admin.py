from django.contrib import admin

from .models import Post, Comment, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'created_at'
    )
    ordering = ('created_at',)
    list_filter = ('title',)
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}



class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'intro',
        'body',
        'category',
        'status',
        'created_at',
        'image'
    )
    ordering = ('created_at', 'status')
    list_filter = ('title', 'status')
    search_fields = ['slug', 'status']
    inlines = (CommentItemInline,)
    prepopulated_fields = {'slug': ('title', )}


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'body',
        'post',
        'created_at'
    )
    ordering = ('created_at',)
    list_filter = ('name',)
    search_fields = ['name', 'email']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
