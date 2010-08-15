from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^add/(?P<slug>\S+)$','users.views.users_add', name='users_add'),
)