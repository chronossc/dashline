from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import RequestContext
from models import TimeLine, Entry
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from forms import TimeLineForm
from django.forms.models import inlineformset_factory

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
    """ Adds one entry to a timeline. AJAX stuff """
    #TODO
    pass


@login_required
def create_timeline(request):
    """ Creates a timeline. """
    form = TimeLineForm()
    
    if request.method == 'POST':
        form = TimeLineForm(request.POST)
        
        if form.is_valid():          
            curr = form.save(commit=False)
            curr.owner = request.user
            curr.save()
            return HttpResponseRedirect(reverse('timeline_add_entries', args=[curr.slug]))                                        
        
    return render_to_response('timeline/create.html', {'form': form}, context_instance=RequestContext(request))


@login_required
def add_entries(request, slug):
    """ First way to add entries do a timeline """
    timeline = get_object_or_404(TimeLine, slug=slug, owner=request.user)
    
    AddEntryFormset = inlineformset_factory(TimeLine, Entry, extra=0)

    # if this form has been submitted..
    if request.method == 'POST':
        if 'add_entry' in request.POST:
            cp = request.POST.copy()
            cp['timeline-TOTAL_FORMS'] = int(cp['timeline-TOTAL_FORMS'])+ 1
            new_entry = AddEntryFormset(cp, prefix='timeline', instance=timeline)
            
        elif 'submit' in request.POST:
            formset = AddEntryFormset(request.POST, instance=timeline)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Timeline created successfuly.')
                return HttpResponseRedirect(reverse('timeline_show', args=[timeline.slug]))
        
    #if it's a fresh form
    else:
        new_entry = AddEntryFormset(prefix='timeline', instance=timeline)
    
    # return the rendered template
    return render_to_response('timeline/add_entry.html', {'timeline':new_entry}, context_instance=RequestContext(request))
    

def get_hottest(request):
    """ Returns the most viewed/commented timelines """
    #TODO
    pass


def get_lastest(request):
    """ Returns the lastest timelines created """
    timelines = TimeLine.objects.filter().order_by(['-id'])[:15]
    return render_to_response('timeline/lastest.html', {'timelines': timelines}, context_instance=RequestContext(request))


def browse_timelines(request, *args, **kwargs):
    """ Browse all timelines available in the site. """
    timeline = TimeLine.objects.all()

    return render_to_response('timeline/browse.html',
                              {"timelines": timeline },
                              context_instance=RequestContext(request))
