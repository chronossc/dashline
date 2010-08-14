from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import TimeLine, Entry
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def show_timeline(request, slug):
    """ View that returns a timeline or a 404 error if the timeline cannot be found """
    timeline = get_object_or_404(TimeLine, slug=slug)
    return render_to_response('timeline/show.html', {'timeline': timeline}, context_instance=RequestContext(request))


def show_entry(request):
    """ Shows detailed info about one entry inside a timeline. AJAX stuff """
    #TODO
    pass

@login_required
def post_entry(request):
    """ Adds one entry to a timeline """
    #TODO
    pass

@login_required
def create_timeline(request):
    """ Creates a timeline. """
    #TODO
    pass

def get_hottest(request):
    """ Returns the most viewed/commented timelines """
    #TODO
    pass

def get_lastest(request):
    """ Returns the lastest timelines created """
    timelines = TimeLine.objects.filter().order_by(['-id'])[:15]
    return render_to_response('timeline/lastest.html', {'timelines': timelines}, context_instance=RequestContext(request))

def browse_timelines(request):
    timeline = TimeLine.objects.all()
    paginator = Paginator(timeline, 15) # Show 15 contacts per page

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        timelines = paginator.page(page)
    except (EmptyPage, InvalidPage):
        timelines = paginator.page(paginator.num_pages)

    return render_to_response('timeline/browse.html', {"timelines": paginator}, context_instance=RequestContext(request))