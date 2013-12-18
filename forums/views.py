from django.shortcuts import render

# Create your views here.
from forums.models import Users, Topics, Comments, Replies
from forums.serializers import UserSerializer, TopicSerializer, CommentsSerializer, RepliesSerializer
from rest_framework import generics

"""
    Generic Views:
    
    The generic views below provided by the REST framework allows you to build API views
    that map closely to your database models.
    
"""

class Register(generics.CreateAPIView):
    """
        CreateAPIView: Used for create-only.
        
    """
    serializer_class = UserSerializer
    
class UserList(generics.ListAPIView):
    """
       ListAPIView: Used for read-only, to represent a collection of model instances.
       
       Example to view a specific user: /users/{id}
       
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView: Used for read-write-delete, to represent a single model instance.
        
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    
class TopicList(generics.ListCreateAPIView):
    """
        ListCreateAPIView: Used for read-write, to represent a collection of model instances.
        
        Below is a representation of the:
            id: The unique id for the topic
            title: The title of the topic
            owner: The user that created the topic
        
        Example to view a specific topic: /topics/{id}
    """
    queryset = Topics.objects.all()
    serializer_class = TopicSerializer

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView: Used for read-write-delete, to represent a single model instance.
        
    """
    queryset = Topics.objects.all()
    serializer_class = TopicSerializer
    
class CommentList(generics.ListCreateAPIView):
    """
        ListCreateAPIView: Used for read-write, to represent a collection of model instances.
        
        Below is a representation of the:
            id: The unique id for the topic
            comment: The title of the topic
            topic: The user that created the topic
            owner: The user that created the comment
        
        Example to view a specific comment: /comment/{id}
        
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView: Used for read-write-delete, to represent a single model instance.
        
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    
class ReplyList(generics.ListCreateAPIView):
    """
        ListCreateAPIView: Used for read-write, to represent a collection of model instances.
        
        Example to view a specific reply: /reply/{id}
    """
    queryset = Replies.objects.all()
    serializer_class = RepliesSerializer

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView: Used for read-write-delete, to represent a single model instance.
        
    """
    queryset = Replies.objects.all()
    serializer_class = RepliesSerializer