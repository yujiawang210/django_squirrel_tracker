from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):

    latitude = models.FloatField(
            help_text = _("Latitude"),
            )

    longitude = models.FloatField(
            help_text = _("Longitude"),
            )

    unique_squirrel_id = models.CharField(
            max_length=20,
            help_text = _("Unique_Squirrel_ID"),
            unique = True,
            )

    PM = 'PM'
    AM = 'AM'

    SHIFT_CHOICES  = (
            (PM, 'PM'),
            (AM, 'AM'),
            ('','---'),
            )

    shift = models.CharField(
            max_length = 10,
            choices = SHIFT_CHOICES,
            default = '',
            )

    date = models.DateField(
            help_text = _('Date'),
            )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            ('?', '---'),
            ('', '---'),
          )

    age = models.CharField(
            max_length = 10,
            choices = AGE_CHOICES,
            default = '',
            blank = True,
            )

    BLACK = 'Black'
    CINNAMON = 'Cinnamon'
    GRAY = 'Gray'

    COLOR_CHOICES = (
            (BLACK, 'Black'),
            (CINNAMON, 'Cinnamon'),
            (GRAY, 'Gray'),
            ('', '---'),
            )

    primary_fur_color = models.CharField(
            max_length = 20,
            choices = COLOR_CHOICES,
            default = '',
            blank = True,
            )

    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'

    LOCATION_CHOICES = (
            (ABOVE_GROUND, 'Above Ground'),
            (GROUND_PLANE, 'Ground Plane'),
            ('', '---'),
            )

    location = models.CharField(
            max_length = 20,
            choices = LOCATION_CHOICES,
            default = '',
            blank = True,
            )

    specific_location = models.CharField(
            max_length = 100,
            help_text = _('Specific location'),
            blank = True,
            )

    running = models.BooleanField(
            default = False,
            help_text = _('Running'),
            )

    chasing = models. BooleanField(
            default = False,
            help_text = _('Chasing'),
            )

    climbing = models.BooleanField(
            default = False,
            help_text = _('Climbing'),
            )

    eating  = models.BooleanField(
            default = False,
            help_text = _('Eating'),
            )

    foraging = models.BooleanField(
            default = False,
            help_text = _('Foraging'),
            )

    other_activities = models.CharField(
            max_length = 100,
            help_text = _('Other Activities'),
            blank = True
            )

    kuks = models.BooleanField(
            default = False,
            help_text = _ ('Kuks'),
            )

    quaas = models.BooleanField(
            default = False,
            help_text = _('Quaas'),
            )

    moans = models.BooleanField(
            default = False,
            help_text = _('Moans'),
            )

    tail_flags = models.BooleanField(
            default = False,
            help_text = _('Tail_flags'),
            )

    tail_twitches = models.BooleanField(
            default = False,
            help_text = _('Tail_twitches'),
            )

    approaches = models.BooleanField(
            default = False,
            help_text = _('Approach'),
            )

    indifferent = models.BooleanField(
            default = False,
            help_text = _('Indifferent'),
            )

    runs_from = models.BooleanField(
            default = False,
            help_text = _('Runs from'),
            )


    def __str__(self):
        return self.unique_squirrel_id



