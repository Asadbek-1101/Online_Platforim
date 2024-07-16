from django.contrib import admin

from .models import User, Course, Lesson, Comment, Like

admin.site.register([User, Course])

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class LikeInline(admin.StackedInline):
    model = Like
    extra = 0

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'video', 'created')
    list_display_links = ('name',)
    list_filter = ('created',)
    search_fields = ('name', 'created')
    inlines = [
        CommentInline,
        LikeInline
    ]
