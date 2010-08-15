from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^follow/(?P<slug>\S+)$','users.views.users_follow', name='users_follow'),
    url(r'^unfollow/(?P<slug>\S+)$','users.views.users_unfollow', name='users_unfollow'),
)