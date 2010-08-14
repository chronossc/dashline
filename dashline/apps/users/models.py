from django.db import models
from django.contrib.auth.models import User
from apps.timeline.models import TimeLine

class UserProfile(models.Model):
    timelines = models.ForeignKey(TimeLine)
    user = models.ForeignKey(User, unique=True)
