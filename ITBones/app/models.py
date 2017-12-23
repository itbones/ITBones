"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class admin_visitor(models.Model):
    ip_add = models.CharField(max_length=100,blank=True)
    viewname  = models.CharField(max_length=100,blank=True)
    userid = models.CharField(max_length=100,blank=True)
    logstamp = models.CharField(max_length=100,blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.userid
