# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from apps.timeline.models import TimeLine, Entry

def user_post_save(**kwargs):
    """
    This method should create a entry in UserProfile for each user created, and
    then create a default and empty timeline
    """
    # import here to avoid cross import issues
    from apps.users.models import UserProfile
    
    instance = kwargs.pop('instance')
    created = kwargs.pop('created')
    
    # add user profile if not exists
    try:
        profile = instance.userprofile_set.get()
    except UserProfile.DoesNotExist:
        profile = instance.userprofile_set.create(user=instance.id)
        profile.save()
    
    # add a default timeline if not exists
    if instance.timelines.count() == 0:
        t = instance.timelines.create(
            owner = instance.id,
            title = _('playground'),
            description  = _('This is %s first timeline :). It is intended to'\
                'be use as a playground.') % instance.username,
            default_timeline=True
        )
        t.save()

