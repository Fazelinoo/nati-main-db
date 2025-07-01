from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.TextChoices):
    ADMIN = 'admin', 'admin'
    MUSIC_PRODUCER = 'music_producer', 'music producer'
    GAME_DEVELOPERS = 'game_developer', 'game developer'
    IT = 'it', 'IT'


class CustomUser(AbstractUser):

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.ADMIN)
    last_seen = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

