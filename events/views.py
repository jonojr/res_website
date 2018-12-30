import datetime

from django.shortcuts import get_object_or_404, render
from .models import Event


def index(request):
    now = datetime.datetime.now()
    events = Event.objects.filter(end_time_and_date__gte=now).order_by('start_time_and_date')
    return render(request, 'events_overview.html', {'event_list': events, })


def details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    start = event.start_time_and_date.strftime('%Y%m%dT%H%M%S')
    end = event.end_time_and_date.strftime('%Y%m%dT%H%M%S')
    link = f'http://www.google.com/calendar/event?action=TEMPLATE&text={event.name}&dates={start}/{end}&details={event.information}&location={event.location}&trp=false&sprop=&sprop=name:'
    return render(request, 'event_details.html', {'event': event, 'link': link})
