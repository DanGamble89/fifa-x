from datetime import date
from django.contrib.postgres.fields import ArrayField
from django.db import models

from ..clubs.models import Club
from ..leagues.models import League
from ..nations.models import Nation
from fifa.models import TimeStampedModel, EaModel


PLAYER_POSITION_CHOICES = (
    ('gk', 'GK'),
    ('rwb', 'RWB'),
    ('rb', 'RB'),
    ('cb', 'CB'),
    ('lb', 'LB'),
    ('lwb', 'LWB'),
    ('cdm', 'CDM'),
    ('cm', 'CM'),
    ('cam', 'CAM'),
    ('rm', 'RM'),
    ('rw', 'RW'),
    ('rf', 'RF'),
    ('lm', 'LM'),
    ('lw', 'LW'),
    ('lf', 'LF'),
    ('cf', 'CF'),
    ('st', 'ST')
)

PLAYER_POSITION_LINE_CHOICES = (
    ('gk', 'GK'),
    ('def', 'DEF'),
    ('mid', 'MID'),
    ('att', 'ATT')
)

PLAYER_WORKRATE_CHOICES = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
)

PLAYER_POSITION_LINES = {
    'GK': ['GK'],
    'DEF': ['RB', 'RWB', 'CB', 'LB', 'LWB'],
    'MID': ['CDM', 'CM', 'CAM', 'RM', 'RW', 'LM', 'LW'],
    'ATT': ['CF', 'ST', 'RF', 'LF']
}


class Player(TimeStampedModel, EaModel):
    # Names
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    common_name = models.CharField(max_length=255)

    # Django's
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)

    # Relations
    club = models.ForeignKey(Club)
    league = models.ForeignKey(League)
    nation = models.ForeignKey(Nation)

    # Images
    image_small = models.CharField(max_length=500)
    image_medium = models.CharField(max_length=500)
    image_large = models.CharField(max_length=500)

    # Positions
    position = models.CharField(max_length=3, choices=PLAYER_POSITION_CHOICES)
    position_line = models.CharField(max_length=3, choices=PLAYER_POSITION_LINE_CHOICES)
    position_full = models.CharField(max_length=3)

    # Personal
    birthdate = models.DateField()
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()

    # Stats
    acceleration = models.PositiveIntegerField()
    aggression = models.PositiveIntegerField()
    agility = models.PositiveIntegerField()
    balance = models.PositiveIntegerField()
    ball_control = models.PositiveIntegerField()
    skill = models.PositiveIntegerField()
    weak_foot = models.PositiveIntegerField()
    crossing = models.PositiveIntegerField()
    curve = models.PositiveIntegerField()
    dribbling = models.PositiveIntegerField()
    finishing = models.PositiveIntegerField()
    free_kick_accuracy = models.PositiveIntegerField()
    gk_diving = models.PositiveIntegerField()
    gk_handling = models.PositiveIntegerField()
    gk_kicking = models.PositiveIntegerField()
    gk_positioning = models.PositiveIntegerField()
    gk_reflex = models.PositiveIntegerField()
    heading_accuracy = models.PositiveIntegerField()
    interceptions = models.PositiveIntegerField()
    jumping = models.PositiveIntegerField()
    long_passing = models.PositiveIntegerField()
    long_shots = models.PositiveIntegerField()
    marking = models.PositiveIntegerField()
    penalties = models.PositiveIntegerField()
    positioning = models.PositiveIntegerField()
    potential = models.PositiveIntegerField()
    reactions = models.PositiveIntegerField()
    short_passing = models.PositiveIntegerField()
    shot_power = models.PositiveIntegerField()
    sliding_tackle = models.PositiveIntegerField()
    sprint_speed = models.PositiveIntegerField()
    standing_tackle = models.PositiveIntegerField()
    stamina = models.PositiveIntegerField()
    strength = models.PositiveIntegerField()
    vision = models.PositiveIntegerField()
    volleys = models.PositiveIntegerField()
    preferred_foot = models.CharField(max_length=255)

    # Descriptions
    traits = ArrayField(models.TextField(max_length=255, blank=True, null=True), blank=True, null=True)
    specialities = ArrayField(models.TextField(max_length=255, blank=True, null=True), blank=True, null=True)

    # Workrates
    workrate_att = models.CharField(max_length=10, choices=PLAYER_WORKRATE_CHOICES)
    workrate_def = models.CharField(max_length=10, choices=PLAYER_WORKRATE_CHOICES)

    # Card stats
    card_att_1 = models.PositiveIntegerField()
    card_att_2 = models.PositiveIntegerField()
    card_att_3 = models.PositiveIntegerField()
    card_att_4 = models.PositiveIntegerField()
    card_att_5 = models.PositiveIntegerField()
    card_att_6 = models.PositiveIntegerField()
    overall_rating = models.PositiveIntegerField()

    # Misc
    ea_id_unique = models.CharField(max_length=255)
    play_style = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)

    player_type = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    is_goalkeeper = models.BooleanField(default=False)
    is_special_type = models.BooleanField(default=False)
    is_fut_player = models.BooleanField(default=False)

    class Meta:
        ordering = ('order', 'overall_rating', 'common_name', 'pk')
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return self.common_name

    def age(self):
        # Might be able to get an age from Postgres age(), use this for now
        today = date.today()

        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
