from django.db import models
import datetime

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.username, self.password)
    
class Topics(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(Users)
    datecreated = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.title, self.owner, self.datecreated)

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=100)
    topic = models.ForeignKey(Topics)
    datecreated = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.comment, self.topic, self.datecreated)

class Replies(models.Model):
    id = models.AutoField(primary_key=True)
    replies = models.CharField(max_length=100)
    comment = models.ForeignKey(Comments)
    datecreated = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.comment, self.comment, self.datecreated)