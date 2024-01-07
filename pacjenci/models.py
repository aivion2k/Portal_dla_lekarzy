from django.db import models
from django.conf import settings


class Pacjent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    imie = models.CharField(max_length=100, default='')
    nazwisko = models.CharField(max_length=100, default='')
    pesel = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    def get_full_name(self):
        return f"{self.imie} {self.nazwisko}"


