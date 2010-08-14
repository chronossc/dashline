from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    url(r'^show/(?P<slug>\S+)$','timeline.views.show_timeline', name='timeline_show'),
    url(r'^create/$','timeline.views.create_timeline', name='timeline_create'),
    url(r'^browse/$','timeline.views.browse_timelines', name='timeline_browse'),
    url(r'^add_entries/(?P<slug>\S+)$','timeline.views.add_entries', name='timeline_add_entries'),
)
