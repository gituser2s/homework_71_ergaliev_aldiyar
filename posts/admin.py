from django.contrib import admin
from posts.models.posts import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'likes_count', 'description', 'image', 'author', 'is_deleted')
    list_filter = ('id', 'likes_count', 'description', 'image', 'author', 'is_deleted')
    search_fields = ('likes_count', 'description', 'image', 'author')
    fields = ('likes_count', 'description', 'image', 'author')
    readonly_fields = ('id', 'is_deleted')


admin.site.register(Post, PostAdmin)
