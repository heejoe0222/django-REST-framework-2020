from django.contrib import admin
from api.models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'likes_count', 'created_at', 'updated_at')
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'text', 'likes_count', 'created_at', 'updated_at')
