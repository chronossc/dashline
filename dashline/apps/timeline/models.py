from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

TYPE_CHOICES = (
    ('URL', _('Link to another site')),
    ('VIDEO', _('Video on YouTube')),
    ('IMG', _('Picture')),
    ('TXT', _('Plain Text')),
)

ORDERING_CHOICES = (
    ('Y', _('Year')),
    ('M', _('Month')),
    ('D', _('Day')),
)

class TimeLine(models.Model):
    """Class that contains base information for our timeline application."""
    owner = models.ForeignKey(User, related_name='timelines')
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    date_created = models.DateTimeField(_("Date created"), auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True)
    default_ordering = models.CharField(_("Default ordering"), choices=ORDERING_CHOICES, max_length=2)
    default_timeline = models.BooleanField(default=False,blank=True)

    class Meta:
        ordering = ('date_created', 'title')

    def __unicode__(self):
        return "(%s) %s - %s" % (self.owner.username, self.title, self.date_created)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        counter = 1

        while True:
            try:
                tl = TimeLine.objects.get(slug=self.slug)
                if tl == self:
                    super(TimeLine, self).save(*args, **kwargs)
                    break

                self.slug += str(counter)
                counter += 1
            except TimeLine.DoesNotExist:
                super(TimeLine, self).save(*args, **kwargs)
                break

    def get_absolute_url(self):
        return reverse('timeline.views.show_timeline', args=[self.slug])



class Entry(models.Model):
    """Represents one entry inside a timeline."""
    timeline = models.ForeignKey(TimeLine)
    title = models.CharField(_("Title"), max_length=255)
    when = models.DateTimeField(_("Entry date"),)
    #icon = models.TextField() #TODO implement
    entry_type = models.CharField(_("Entry type"), choices=TYPE_CHOICES, max_length=10)
    description = models.CharField(_("Entry description"), max_length=255)
    entry_content = models.TextField(_("Entry content"), )
    
    class Meta:
        ordering = ('when', 'title')
    
    def __unicode__(self):
        return "(%s) %s - %s" % (self.timeline, self.title, self.when)
