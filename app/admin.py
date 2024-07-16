from django.contrib import admin

from .models import User, Course, Lesson, Comment, Like

admin.site.register([User, Course, Lesson, Comment, Like])

class Comment(admin.TabularInline):
    model = Comment
    extra = 0

class Like(admin.TabularInline):
    model = Like
    extra = 0

class Lesson(admin.ModelAdmin):
    list_display = ('name', 'video', 'created')
    list_editable = ('name',)
    inlines = [
        Comment,
        Like
    ]




