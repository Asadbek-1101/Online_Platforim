from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Course, Lesson, Comment, Like

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()
