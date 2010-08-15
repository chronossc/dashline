from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from models import Follow
from django.contrib.auth.models import User

@login_required
def users_follow(request, *args, **kwargs):
    username = kwargs.get('slug', '')
    friend = get_object_or_404(User, username=username)
    follow = Follow(from_user=request.user, to_user=friend)
    follow.save()
    messages.add_message(request, messages.INFO, 'You are now following %s' % friend.username)
    return reverse('profiles_profile_detail', args=[friend.username])
