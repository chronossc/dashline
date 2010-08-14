from django.db import models
from django.contrib.auth.models import User
from apps.timeline.models import Timeline

class Profile(User):
    timelines = models.ManyToMany(Timeline)