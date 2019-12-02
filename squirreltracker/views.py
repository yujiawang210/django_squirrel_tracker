from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.forms import ModelForm

from .models import Sighting

# Create sighting form
class SightingForm(ModelForm):
    class Meta:
        model=Sighting
        fields=[
                "latitude",
                "longitude",
                "unique_squirrel_id",
                "shift",
                "date",
                "age",
                "primary_fur_color",
                "location",
                "specific_location",
                "running",
                "chasing",
                "climbing",
                "eating",
                "foraging",
                "other_activities",
                "kuks",
                "quaas",
                "moans",
                "tail_flags",
                "tail_twitches",
                "approaches",
                "indifferent",
                "runs_from"
                ]

# View: List of all sightings
def all_sightings(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request, 'squirreltracker/sightings.html', context)

# View: Create new sighting
def sighting_create(request):
    form = SightingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_sightings')
    return render(request, 'squirreltracker/create_sighting.html', {'create_sighting':form})

# View: Update sighting
def sighting_update(request,unique_squirrel_id):
   sighting = get_object_or_404(Sighting, unique_squirrel_id=unique_squirrel_id)
   form = SightingForm(request.POST or None, instance=sighting)
   if 'Update' in request.POST:
       if form.is_valid():
           form.save()
           return redirect('all_sightings')
   elif 'Delete' in request.POST:
       sighting.delete()
       return redirect('all_sightings')
   elif 'Cancel' in request.POST:
        return redirect('all_sightings')
   return render(request, 'squirreltracker/update_sighting.html', {'create_sighting':form})

# Create markers on map
def map(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request, 'squirreltracker/map.html',context)


