from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from fifa.apps.models import TimeStampedModel
from fifa.apps.players.models import Player


FORMATION_CHOICES = (
    ('3412', '3-4-1-2'),
    ('3421', '3-4-2-1'),
    ('343', '3-4-3'),
    ('352', '3-5-2'),
    ('41212', '4-1-2-1-2'),
    ('41212-2', '4-1-2-1-2 (2)'),
    ('4141', '4-1-4-1'),
    ('4231', '4-2-3-1'),
    ('4231-2', '4-2-3-1 (2)'),
    ('4222', '4-2-2-2'),
    ('4312', '4-3-1-2'),
    ('4321', '4-3-2-1'),
    ('433', '4-3-3'),
    ('433-2', '4-3-3 (2)'),
    ('433-3', '4-3-3 (3)'),
    ('433-4', '4-3-3 (4)'),
    ('433-5', '4-3-3 (5)'),
    ('4411', '4-4-1-1'),
    ('442', '4-4-2'),
    ('442-2', '4-4-2 (2)'),
    ('451', '4-5-1'),
    ('451-2', '4-5-1 (2)'),
    ('5212', '5-2-1-2'),
    ('5221', '5-2-2-1'),
    ('532', '5-3-2')
)


class Squad(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True, unique=True)
    players = models.ManyToManyField(Player, through='SquadLocation')
    formation = models.CharField(
        max_length=10,
        choices=(
            ('3412', '3-4-1-2'),
            ('3421', '3-4-2-1'),
            ('343', '3-4-3'),
            ('352', '3-5-2'),
            ('41212', '4-1-2-1-2'),
            ('41212-2', '4-1-2-1-2 (2)'),
            ('4141', '4-1-4-1'),
            ('4231', '4-2-3-1'),
            ('4231-2', '4-2-3-1 (2)'),
            ('4222', '4-2-2-2'),
            ('4312', '4-3-1-2'),
            ('4321', '4-3-2-1'),
            ('433', '4-3-3'),
            ('433-2', '4-3-3 (2)'),
            ('433-3', '4-3-3 (3)'),
            ('433-4', '4-3-3 (4)'),
            ('433-5', '4-3-3 (5)'),
            ('4411', '4-4-1-1'),
            ('442', '4-4-2'),
            ('442-2', '4-4-2 (2)'),
            ('451', '4-5-1'),
            ('451-2', '4-5-1 (2)'),
            ('5212', '5-2-1-2'),
            ('5221', '5-2-2-1'),
            ('532', '5-3-2')
        )
    )
    chemistry = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    rating = models.DecimalField(
        default=0,
        decimal_places=1,
        max_digits=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    attack = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    midfield = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    defence = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    pace = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    shooting = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    passing = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    dribbling = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    defending = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    physical = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        return self.name


class SquadLocation(models.Model):
    player = models.ForeignKey(Player)
    squad = models.ForeignKey(Squad)
    position = models.CharField(max_length=3)
