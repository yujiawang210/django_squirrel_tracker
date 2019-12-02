from squirreltracker.models import Sighting
  
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):

        fields = Sighting._meta.get_fields()
        sightings = Sighting.objects.all()

        path = kwargs['path']
        writer = csv.writer(open(path,'w'))

        headers = []
        for field in fields:
            headers.append(field.name)
        writer.writerow(headers)

        for sighting in sightings:
            writer.writerow([
                    sighting.latitude,
                    sighting.longitude,
                    sighting.unique_squirrel_id,
                    sighting.shift,
                    sighting.date,
                    sighting.age,
                    sighting.primary_fur_color,
                    sighting.location,
                    sighting.specific_location,
                    sighting.running,
                    sighting.chasing,
                    sighting.climbing,
                    sighting.eating,
                    sighting.foraging,
                    sighting.other_activities,
                    sighting.kuks,
                    sighting.quaas,
                    sighting.moans,
                    sighting.tail_flags,
                    sighting.tail_twitches,
                    sighting.approaches,
                    sighting.indifferent,
                    sighting.runs_from
                    ])

