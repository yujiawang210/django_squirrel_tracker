from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.forms import ModelForm

from .models import Sighting

# View: List of all sightings
def all_sightings(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
<<<<<<< HEAD
    return render(request, 'SquirrelTracker/sightings.html', context)
=======
    return render(request, 'squirreltracker/sightings.html', context)
>>>>>>> 4c93dbe3bcb5f5b44193c1a91fe85f925c586994

# Create markers on map
def map(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
<<<<<<< HEAD
    return render(request, 'SquirrelTracker/map.html',context)
=======
    return render(request, 'squirreltracker/map.html',context)
>>>>>>> 4c93dbe3bcb5f5b44193c1a91fe85f925c586994
