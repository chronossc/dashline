import haystack
haystack.autodiscover()

import datetime
from haystack.indexes import *
from haystack import site
from timeline.models import TimeLine
from users.models import UserProfile


class TimeLineIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    owner = CharField(model_attr='owner')


class UserProfileIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    user = CharField(model_attr='user')


site.register(TimeLine, TimeLineIndex)
site.register(UserProfile, UserProfileIndex)
