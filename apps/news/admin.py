from django.contrib import admin
from .models import News, Comment, Status, CommentStatus, NewsStatus


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsStatus)
class NewsStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentStatus)
class StatusCommentAdmin(admin.ModelAdmin):
    verbose_name_plural = "comment reactions"


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass

