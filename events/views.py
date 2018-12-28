from django.shortcuts import render
from .models import Event


def index(request):
    events = Event.objects.all()
    return render(request, 'events_overview.html', {'events': events, })
