from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Course(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    about_course = models.TextField()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    video = models.FileField(upload_to='lesson/video/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'ogg', 'avi', 'wmv'])
    ]) #Turli formatdagi ma'lumotlarni qabul qilish uchun
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Comment by {self.lesson.name}'

class Like(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like_or_dislike = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like/Dislike by {self.lesson.name}'
