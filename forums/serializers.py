from django.forms import widgets
from rest_framework import serializers
from forums.models import Users, Topics

class ForumsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ('id', 'username', 'password', 'datecreated')
    

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new user instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.wa
        """
        if instance:
            # Update existing instance
            instance.username = attrs.get('username', instance.username)
            instance.password = attrs.get('password', instance.password)
            return instance

        # Create new instance
        return Users(**attrs)
    
class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topics
        fields = ('id', 'title', 'owner', 'datecreated')
    
    def restore_object(self, attrs, instance=None):
        """
        Create or update a new user instance, given a dictionary
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