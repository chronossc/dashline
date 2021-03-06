import urllib
import hashlib

from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from apps.timeline.models import TimeLine
from apps.users import signals as users_signals
from apps.utils import fields
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse


class Follow(models.Model):
  from_user = models.ForeignKey(User, related_name='following_set')
  to_user = models.ForeignKey(User, related_name='followers_set')
  
  def __unicode__(self):
    return u'%s, %s' % (self.from_user.username, self.to_user.username)
  
  class Meta:
    unique_together = (('to_user', 'from_user'), )


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    country = fields.CountryField(_('Country'))
    description = models.TextField(_('Description'), blank=True)
    twitter = models.URLField(blank=True)

    @property
    def avatar(self):
        size = 48
        email = self.user.email
        default = "http://www.wprecipes.com/wp-content/uploads/2009/01/gravatar1.jpg"
        url = "http://www.gravatar.com/avatar.php?%s" % urllib.urlencode({
                                                                        'gravatar_id': hashlib.md5(email).hexdigest(),
                                                                        'default': default,
                                                                        'size': str(size) })
        return '<img width="%s" src="%s" alt="%s"></img>' % (size, url, size)
    
    def __unicode__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profiles_profile_detail', args=[self.user.username])

signals.post_save.connect(users_signals.user_post_save,User)


