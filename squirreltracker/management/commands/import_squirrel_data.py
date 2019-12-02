from squirreltracker.models import Sighting

from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                latitude = row['Y']
                longitude = row['X']
                unique_squirrel_id = row['Unique Squirrel ID']
                shift = row['Shift']
                date = row['Date']
                date = datetime.datetime.strptime(date, '%m%d%Y')
                age = row['Age']
                primary_fur_color = row['Primary Fur Color']
                location = row['Location']
                specific_location = row['Specific Location']
                running = row['Running'].capitalize()
                chasing = row['Chasing'].capitalize()
                climbing = row['Climbing'].capitalize()
                eating = row['Eating'].capitalize()
                foraging = row['Foraging'].capitalize()
                other_activities = row['Other Activities']
                kuks = row['Kuks'].capitalize()
                quaas = row['Quaas'].capitalize()
                moans = row['Moans'].capitalize()
                tail_flags = row['Tail flags'].capitalize()
                tail_twitches = row['Tail twitches'].capitalize()
                approaches = row['Approaches'].capitalize()
                indifferent = row['Indifferent'].capitalize()
                runs_from = row['Runs from'].capitalize()

                new_sighting = Sighting(
                    latitude=latitude,
                    longitude=longitude,
                    unique_squirrel_id=unique_squirrel_id,
                    shift=shift,
                    date=date,
                    age=age,
                    primary_fur_color=primary_fur_color,
                    location=location,
                    specific_location=specific_location,
                    running=running,
                    chasing=chasing,
                    climbing=climbing,
                    eating=eating,
                    foraging=foraging,
                    other_activities=other_activities,
                    kuks=kuks,
                    quaas=quaas,
                    moans=moans,
                    tail_flags=tail_flags,
                    tail_twitches=tail_twitches,
                    approaches=approaches,
                    indifferent=indifferent,
                    runs_from=runs_from,
                    )

                try:
                    new_sighting.save()
                except:
                     print("There was a problem with line ", row)


