from django.core.mail import send_mail
from django.conf import settings

from rest_framework.generics import (ListCreateAPIView, RetrieveDestroyAPIView,
                                     RetrieveUpdateDestroyAPIView, GenericAPIView)
from rest_framework import permissions, filters, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Course, Lesson, Comment, Like, User
from .serializers import (CourseSerializer, LessonSerializer, CommentSerializer, LikeSerializer,
                          EmailSerializer)
from .permissions import CoursePermission, LessonPermission

class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [CoursePermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "price", "about_course"]

class CourseListUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [CoursePermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "price", "about_course"]

class LessonCreateAPIView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [LessonPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

class LessonDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [LessonPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

class CommentCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["text"]

class LikeAPIView(APIView):
    def get(self, request, pk):
        likes = Like.objects.filter(like_or_dislike=True, lesson_id=pk).count()
        dis_likes = Like.objects.filter(like_or_dislike=False, lesson_id=pk).count()
        return Response({"likes": likes, "dis_likes": dis_likes})

class LikeCreateView(APIView):
    def post(self, request):
        author_id = request.data.get('author')
        lesson_id = request.data.get('lesson')
        like_or_dislike = request.data.get('like_or_dislike')

        l_or_d = Like.objects.filter(author_id=author_id, lesson_id=lesson_id).first()

        if l_or_d:
            l_or_d.delete()
            if l_or_d.like_or_dislike == like_or_dislike:
                return Response({"message": "Like o'chdi"})

        serializer = LikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_dislike = serializer.save()
        return Response(LikeSerializer(like_dislike).data)


class SendEmailToUserView(APIView):
    def post(self, request: Request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.all()
        user_email = []
        for user in users:
            user_email.append(user.email)
        user_email.append("asadbekshahobiddinov01@gmial.com")

        send_mail(
            serializer.validated_data.get("subject"),
            serializer.validated_data.get("message"),
            settings.EMAIL_HOST_USER,
            user_email,
            fail_silently=False,
        )
        return Response({"message":"Xabar yuborildi."})
