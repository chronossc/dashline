from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$','views.home'),
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True}),
        
    (r'^profiles/', include('profiles.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^timeline/', include('timeline.urls')),
)
