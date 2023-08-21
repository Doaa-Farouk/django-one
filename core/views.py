from django.shortcuts import render
# from django.http import HttpResponse
from .models import Event, Speaker, Sponsor, Accounts, Venue

# Create your views here.

def index(request):
    events = Event.objects.all().values()
    venues = Venue.objects.all().values()
    speakers = Speaker.objects.all().values()
    context = {
        'events' : events,
        'venues' : venues,
        'speakers' : speakers,
    }
    return render(request, "core/index.html", context)