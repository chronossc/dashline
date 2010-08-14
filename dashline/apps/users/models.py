import urllib
import hashlib

from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from apps.timeline.models import TimeLine
from apps.users import signals as users_signals

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

    @property
    def avatar(self):
        size = 48
        email = self.user.email
        default = "http://api.ning.com/files/L-2Mry07IJ3j5NpZFDRiGd2muhP-KJTK*tZ47YoxU2Z2vxpOlFQ4Coi032VORAdYcgx1GXmpfhKedtS9I0gpSoTvg61lWXpX/your_8bit_avatar2.jpg?width=48&height=48&crop=1%3A1"
        url = "http://www.gravatar.com/avatar.php?%s" % urllib.urlencode({
                                                                        'gravatar_id': hashlib.md5(email).hexdigest(), 
                                                                        'default': default, 
                                                                        'size': str(size) })
        gravatar = {'url': url, 'size': size}
        return '<img width="%s" src="%s" alt="%s"></img>' % (size, gravatar['url'], gravatar['size'])

signals.post_save.connect(users_signals.user_post_save,User)
