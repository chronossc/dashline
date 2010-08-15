import haystack
haystack.autodiscover()

import datetime
from haystack.indexes import *
from haystack import site
from timeline.models import TimeLine
from users.models import UserProfile


class TimeLineIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    author = CharField(model_attr='user')
    title = CharField(model_attr='title')
    description = CharField(model_attr='description')


class UserProfileIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    user = CharField(model_attr='user')
    username = CharField(model_attr='user.name')
    twitter = CharField(model_attr='twitter')
    description = CharField(model_attr='description')
    


site.register(TimeLine, TimeLineIndex)
site.register(UserProfile, UserProfileIndex)
