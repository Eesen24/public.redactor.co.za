from django.shortcuts import render

# Create your views here.
from forums.models import Users, Topics, Comments, Replies
from forums.serializers import UserSerializer, TopicSerializer, CommentsSerializer, RepliesSerializer
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    
class TopicList(generics.ListCreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicSerializer

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicSerializer
    
class CommentList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    
class ReplyList(generics.ListCreateAPIView):
    queryset = Replies.objects.all()
    serializer_class = RepliesSerializer

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Replies.objects.all()
    serializer_class = RepliesSerializer