from django.forms import widgets
from rest_framework import serializers
from forums.models import Topics, Comments, Replies, CustomUser
from django.contrib.auth.models import User
"""
    Below is a list of serializer classes. This is a way of serializing and deserializing
    data into representations such as json.
"""
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password')
    
class TopicSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    class Meta:
        model = Topics
        fields = ('id', 'title', 'owner')
    
    def restore_object(self, attrs, instance=None):
        """
        Create or update a new topic instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.owner = attrs.get('owner', instance.owner)
            return instance

        # Create new instance
        return Topics(**attrs)
    
class CommentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields = ('id', 'comment', 'topic', 'owner')
    
    def restore_object(self, attrs, instance=None):
        """
        Create or update a new comment instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.comment = attrs.get('comment', instance.comment)
            instance.topic = attrs.get('topic', instance.topic)
            instance.owner = attrs.get('owner', instance.owner)
            return instance

        # Create new instance
        return Comments(**attrs)
    
class RepliesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Replies
        fields = ('id', 'replies', 'comment', 'owner')
    
    def restore_object(self, attrs, instance=None):
        """
        Create or update a new reply instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.replies = attrs.get('replies', instance.replies)
            instance.comment = attrs.get('comment', instance.comment)
            instance.owner = attrs.get('owner', instance.owner)
            return instance

        # Create new instance
        return Replies(**attrs)