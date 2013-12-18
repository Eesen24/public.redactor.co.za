from django.db import models
import datetime
from django.contrib.auth.models import User, UserManager
"""
    Below are the Model definitions used within the App:
    Model: Users, Topics, Comments, Replies
"""

# Create your models here.
class CustomUser(User):
    """User with app settings."""
    #timezone = models.CharField(max_length=50, default='Europe/London')

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()
    
class Topics(models.Model):
    """
        Stores the topic title and the user as a foreign key
        :model:`Topics`.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    #owner = models.ForeignKey(Users)
    owner = models.ForeignKey('auth.User', related_name='topics')
    
    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.title, self.owner)
    
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        super(Topics, self).save(*args, **kwargs)

class Comments(models.Model):
    """
        Stores the the comments for each topic.Topic is the foreign key.
        :model:`Comments`.
    """
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=100)
    topic = models.ForeignKey(Topics)
    owner = models.ForeignKey(CustomUser)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.comment, self.topic)

class Replies(models.Model):
    """
        Stores the the reply for each comment.Comment is the foreign key.
        :model:`Replies`.
    """
    id = models.AutoField(primary_key=True)
    replies = models.CharField(max_length=100)
    comment = models.ForeignKey(Comments)
    owner = models.ForeignKey(CustomUser)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.comment, self.comment)