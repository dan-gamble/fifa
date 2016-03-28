from django.contrib.postgres.fields import JSONField
from django.core import urlresolvers
from django.db import models
from fifa.apps.models import EaAsset, TimeStampedModel
from ..clubs.models import Club
from ..leagues.models import League
from ..nations.models import Nation

PLAYER_POSITION_CHOICES = (
    ('GK', 'GK'),
    ('RWB', 'RWB'),
    ('RB', 'RB'),
    ('CB', 'CB'),
    ('LB', 'LB'),
    ('LWB', 'LWB'),
    ('CDM', 'CDM'),
    ('CM', 'CM'),
    ('CAM', 'CAM'),
    ('RM', 'RM'),
    ('RW', 'RW'),
    ('RF', 'RF'),
    ('LM', 'LM'),
    ('LW', 'LW'),
    ('LF', 'LF'),
    ('CF', 'CF'),
    ('ST', 'ST')
)

PLAYER_POSITION_LINES = {
    'GK': ['GK'],
    'DEF': ['RB', 'RWB', 'CB', 'LB', 'LWB'],
    'MID': ['CDM', 'CM', 'CAM', 'RM', 'RW', 'LM', 'LW'],
    'ATT': ['CF', 'ST', 'RF', 'LF']
}

PLAYER_POSITION_LINE_CHOICES = (
    ('GK', 'Goalkeepers'),
    ('DEF', 'Defenders'),
    ('MID', 'Midfielders'),
    ('ATT', 'Attackers')
)


class Player(EaAsset, TimeStampedModel, models.Model):
    cached_url = models.CharField(max_length=1000, null=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    club = models.ForeignKey(Club, blank=True, null=True)
    league = models.ForeignKey(League, blank=True, null=True)
    nation = models.ForeignKey(Nation, blank=True, null=True)

    image = models.CharField(max_length=255, blank=True, null=True)
    image_sm = models.CharField(max_length=255, blank=True, null=True)
    image_md = models.CharField(max_length=255, blank=True, null=True)
    image_lg = models.CharField(max_length=255, blank=True, null=True)
    image_special_totw_md = models.CharField(max_length=255, blank=True, null=True)
    image_special_totw_lg = models.CharField(max_length=255, blank=True, null=True)

    position = models.CharField(max_length=3, choices=PLAYER_POSITION_CHOICES, blank=True, null=True)
    position_full = models.CharField(max_length=100, blank=True, null=True)
    position_line = models.CharField(max_length=3, choices=PLAYER_POSITION_LINE_CHOICES, blank=True, null=True)

    playstyle = models.CharField(max_length=100, blank=True, null=True)
    playstyle_id = models.CharField(max_length=100, blank=True, null=True)

    height = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)

    acceleration = models.PositiveIntegerField(blank=True, null=True)
    aggression = models.PositiveIntegerField(blank=True, null=True)
    agility = models.PositiveIntegerField(blank=True, null=True)
    balance = models.PositiveIntegerField(blank=True, null=True)
    ballcontrol = models.PositiveIntegerField(blank=True, null=True)
    crossing = models.PositiveIntegerField(blank=True, null=True)
    curve = models.PositiveIntegerField(blank=True, null=True)
    dribbling = models.PositiveIntegerField(blank=True, null=True)
    finishing = models.PositiveIntegerField(blank=True, null=True)
    freekickaccuracy = models.PositiveIntegerField(blank=True, null=True)
    gkdiving = models.PositiveIntegerField(blank=True, null=True)
    gkhandling = models.PositiveIntegerField(blank=True, null=True)
    gkkicking = models.PositiveIntegerField(blank=True, null=True)
    gkpositioning = models.PositiveIntegerField(blank=True, null=True)
    gkreflexes = models.PositiveIntegerField(blank=True, null=True)
    headingaccuracy = models.PositiveIntegerField(blank=True, null=True)
    interceptions = models.PositiveIntegerField(blank=True, null=True)
    jumping = models.PositiveIntegerField(blank=True, null=True)
    longpassing = models.PositiveIntegerField(blank=True, null=True)
    longshots = models.PositiveIntegerField(blank=True, null=True)
    marking = models.PositiveIntegerField(blank=True, null=True)
    penalties = models.PositiveIntegerField(blank=True, null=True)
    positioning = models.PositiveIntegerField(blank=True, null=True)
    potential = models.PositiveIntegerField(blank=True, null=True)
    reactions = models.PositiveIntegerField(blank=True, null=True)
    shortpassing = models.PositiveIntegerField(blank=True, null=True)
    shotpower = models.PositiveIntegerField(blank=True, null=True)
    slidingtackle = models.PositiveIntegerField(blank=True, null=True)
    sprintspeed = models.PositiveIntegerField(blank=True, null=True)
    standingtackle = models.PositiveIntegerField(blank=True, null=True)
    stamina = models.PositiveIntegerField(blank=True, null=True)
    strength = models.PositiveIntegerField(blank=True, null=True)
    vision = models.PositiveIntegerField(blank=True, null=True)
    volleys = models.PositiveIntegerField(blank=True, null=True)

    foot = models.CharField(max_length=10, blank=True, null=True)
    skill_moves = models.PositiveIntegerField(blank=True, null=True)
    weak_foot = models.PositiveIntegerField(blank=True, null=True)

    traits = JSONField(null=True)
    specialities = JSONField(null=True)

    workrate_att = models.CharField(max_length=10, blank=True, null=True)
    workrate_def = models.CharField(max_length=10, blank=True, null=True)

    player_type = models.CharField(max_length=100, blank=True, null=True)
    item_type = models.CharField(max_length=100, blank=True, null=True)

    overall_rating = models.PositiveIntegerField(blank=True, null=True)
    card_att_1 = models.PositiveIntegerField(blank=True, null=True)
    card_att_2 = models.PositiveIntegerField(blank=True, null=True)
    card_att_3 = models.PositiveIntegerField(blank=True, null=True)
    card_att_4 = models.PositiveIntegerField(blank=True, null=True)
    card_att_5 = models.PositiveIntegerField(blank=True, null=True)
    card_att_6 = models.PositiveIntegerField(blank=True, null=True)

    quality = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)

    is_gk = models.NullBooleanField(default=False)
    is_special_type = models.NullBooleanField(default=False)
    is_loan = models.NullBooleanField(default=False)

    model_name = models.CharField(max_length=100, blank=True, null=True)
    base_id = models.PositiveIntegerField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-overall_rating', '-ea_id']
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return self.common_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Player, self).save()

        self.get_absolute_url(False)

    def get_absolute_url(self, cached=False):
        if self.cached_url and cached:
            return self.cached_url

        url = urlresolvers.reverse('players:player', kwargs={'slug': self.slug})

        if url != self.cached_url:
            self.cached_url = url
            self.save()

        return url
