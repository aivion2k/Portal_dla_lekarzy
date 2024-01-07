from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    jest_lekarzem = models.BooleanField(default=False)
    jest_pacjentem = models.BooleanField(default=False)

    def get_full_name(self):
        if self.jest_lekarzem:
            return self.lekarz.get_full_name()
        elif self.jest_pacjentem:
            return self.pacjent.get_full_name()
        return super().get_full_name()  # Domyślna metoda Django dla AbstractUser

