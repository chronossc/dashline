#!/usr/bin/env python

import os,sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'dashline.settings'

import dashline
sys.path.insert(0,os.path.dirname(dashline.__file__))

from django.contrib.auth.models import User

try:
    u = User.objects.get(username=sys.argv[1])
    u.delete()
except User.DoesNotExist:
    pass


u = User(username=sys.argv[1],email=sys.argv[2])
u.save()
u.set_password(sys.argv[3])
u.save()
