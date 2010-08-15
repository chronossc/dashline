from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404
from models import Friendship

@login_required
def users_add(request, *args, **kwargs):
    try:
        print args
        print kwargs
        import pdb
        pdb.set_trace()
        friend = get_object_or_404(User, username=request.GET['username'])
        friendship = Friendship(from_friend=request.user,to_friend=friend)
        friendship.save()
        messages.add_message(request, messages.INFO, 'Friend added.')
        return HttpResponseRedirect('/friends/%s/' % request.user.username)
    except:
        raise Http404()