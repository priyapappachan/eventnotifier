from django.db import models
from datetime import datetime, time, date, timedelta
# Create your models here.
from django.db.models.signals import post_save
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Poll(models.Model):
    question = models.CharField(max_length=200)
    def __unicode__(self):
        return self.question

class Event(models.Model):
   # typ = models.ForeignKey(Poll)
    eventname = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    event_time = models.TimeField()
    event_date = models.DateField()
   # date = models.DateTimeField('Date Published')
   # eventdate = models.DateTimeField('Event date')
    organizer = models.CharField(max_length=200)
    flag=models.CharField(max_length=200)
    def __unicode__(self):
        return self.eventname

class Blood(models.Model):
	name=models.CharField(max_length=200)
	date=models.DateField()
	group=models.CharField(max_length=3)
	contact=models.CharField(max_length=15)
	organizer=models.CharField(max_length=20)
	def __unicode__(self):
        	return self.name

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    dob = models.CharField(max_length=100)
    blood_group = models.CharField(max_length = 3)
    batch = models.CharField(max_length = 10)
    department = models.CharField(max_length = 100)	
    reg_no = models.CharField(max_length = 100)
    number=models.CharField(max_length=12)
    	
def create_user_profile(sender, instance, created, **kwargs):
    if created:
       	UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)

