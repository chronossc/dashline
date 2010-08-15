import haystack
haystack.autodiscover()

import datetime
from haystack.indexes import *
from haystack import site
from timeline.models import TimeLine
from users.models import UserProfile


class TimeLineIndex(SearchIndex):
    pass


class UserProfileIndex(SearchIndex):
    pass


site.register(TimeLine, TimeLineIndex)
site.register(UserProfile, UserProfileIndex)
