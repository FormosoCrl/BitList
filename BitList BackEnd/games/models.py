from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    # Definimos las opciones de estado
    STATUS_CHOICES = [
        ('NULO', 'Sin estado'),
        ('ACABADO', 'Acabado'),
        ('JUGANDO', 'Jugando'),
        ('NO_JUGADO', 'No jugado'),
        ('PENDIENTE', 'Quiero jugarlo'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    steam_id = models.IntegerField()
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NULO')
    priority = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['priority']


class CustomList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    games = models.ManyToManyField(Game, blank=True)