import datetime
from django.shortcuts import render
from django.apps import apps
from itertools import chain

# Create your views here.

def index(request):
    return render(request, 'tools_index.html')


def slideshow(request):
    event = apps.get_model('events', 'Event')
    events = event.objects.all()

    running_events = [event for event in events if event.currently_running]

    now = datetime.datetime.now()
    end_of_week = now + datetime.timedelta(weeks=1)

    events_this_week = event.objects.filter(start_time_and_date__range=(now, end_of_week))


    all_events = sorted(
        list(chain(events_this_week, running_events)),
        key=lambda instance: instance.start_time_and_date,
    )
    return render(request, 'slideshow.html', {'events': all_events})
