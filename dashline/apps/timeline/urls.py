from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    
    url(r'^show/(?P<slug>\S+)$','timeline.views.show_timeline', name='show'),
    url(r'^create/$','timeline.views.create_timeline', name='create'),
    url(r'^browser/$','timeline.views.browse_timelines', name='browse'),
    
)
