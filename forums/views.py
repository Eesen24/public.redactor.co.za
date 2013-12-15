from django.shortcuts import render

# Create your views here.
from forums.models import Users, Topics
from forums.serializers import ForumsSerializer, TopicSerializer
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = ForumsSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = ForumsSerializer
    
class TopicList(generics.ListCreateAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicSerializer


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topics.objects.all()
    serializer_class = TopicSerializer