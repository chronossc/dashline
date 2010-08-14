from django.db import models
from django.contrib.auth.models import User
from apps.timeline.models import TimeLine

class UserProfile(User):
    timelines = models.ForeignKey(TimeLine)
