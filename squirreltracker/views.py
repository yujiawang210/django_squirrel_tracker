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
    if 'Create' in request.POST:
        if form.is_valid():
            form.save()
            return redirect('all_sightings')
    elif 'Cancel' in request.POST:
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

# View: Sighting stats
def sighting_stats(request):
    from django.db.models import Sum, Count

    total_sightings = Sighting.objects.count()
    AM = Sighting.objects.filter(shift='AM').count()
    PM = Sighting.objects.filter(shift='PM').count()
    Adult = Sighting.objects.filter(age='Adult').count()
    Juvenile = Sighting.objects.filter(age='Juvenile').count()
    color_Gray = Sighting.objects.filter(primary_fur_color='Gray').count()
    color_Black = Sighting.objects.filter(primary_fur_color='Black').count()
    color_Cinnamon = Sighting.objects.filter(primary_fur_color='Cinnamon').count()
    above_ground = Sighting.objects.filter(location='Above Ground').count()
    ground_plane = Sighting.objects.filter(location='Ground Plane').count()
    running_squirrels = Sighting.objects.filter(running=True).count()

    context = {
            'AM' : AM,
            'PM' : PM,
            'total_sightings': total_sightings,
            'Adult': Adult,
            'Juvenile': Juvenile,
            'color_Gray': color_Gray,
            'color_Black': color_Black,
            'color_Cinnamon': color_Cinnamon,
            'above_ground': above_ground,
            'ground_plane': ground_plane,
            'running_squirrels': running_squirrels,
            }

    return render(request, 'squirreltracker/sighting_stats.html', context)

# Create markers on map
def map(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request, 'squirreltracker/map.html',context)


