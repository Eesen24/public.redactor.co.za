from django.db import models
import datetime

"""
    Below are the Model definitions used within the App:
    Model: Users, Topics, Comments, Replies
"""

# Create your models here.
class Users(models.Model):
    """
    Stores a username and password
    :model:`auth.User`.
    """
    #TODO: Need to still figure out how to implement the Django auth 
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.username, self.password)
    
class Topics(models.Model):
    """
        Stores the topic title and the user as a foreign key
        :model:`Topics`.
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(Users)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.title, self.owner)

class Comments(models.Model):
    """
        Stores the the comments for each topic.Topic is the foreign key.
        :model:`Comments`.
    """
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=100)
    topic = models.ForeignKey(Topics)
    
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
    
    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.comment, self.comment)