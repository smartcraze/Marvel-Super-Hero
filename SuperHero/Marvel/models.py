from django.db import models
from django.utils import timezone

# Create your models here.

class Superhero(models.Model):
  HERO_TYPE_CHOICES = [
    ('hero', 'Hero'),
    ('villain', 'Villain'),

  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to=' heros/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=50, choices=HERO_TYPE_CHOICES, default='hero')

  def __str__(self):
    return self.name