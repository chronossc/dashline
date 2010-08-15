from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','views.home', name='views_home'),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True}),
    
    (r'^profiles/', include('profiles.urls')),
    (r'^users/', include('users.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^timeline/', include('timeline.urls')),
    (r'^search/', include('haystack.urls')),
)
