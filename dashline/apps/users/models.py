from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from apps.timeline.models import TimeLine
from apps.users import signals as users_signals

class UserProfile(models.Model):
    timelines = models.ForeignKey(TimeLine)
    user = models.ForeignKey(User, unique=True)

signals.post_save.connect(users_signals.user_post_save,User)
