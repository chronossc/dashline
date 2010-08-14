from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    url(r'^show/(?P<slug>\S+)$','timeline.views.show_timeline', name='timeline_show'),
    url(r'^create/$','timeline.views.create_timeline', name='timeline_create'),
    url(r'^browser/$','timeline.views.browse_timelines', name='timeline_browse'),
    url(r'^add_entries/(?P<slug>\S+)$','timeline.views.browse_timelines', name='timeline_add_entries'),
)
