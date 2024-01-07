from django.db import models
from pacjenci.models import Pacjent
from django.conf import settings
from django.db import models


class Lekarz(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    imie = models.CharField(max_length=100, default='')
    nazwisko = models.CharField(max_length=100, default='')
    specjalizacja = models.CharField(max_length=100)
    numer_pwz = models.CharField(max_length=7, unique=True, default='0000000')
    # Dodaj więcej pól według potrzeb

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    def get_full_name(self):
        return f"{self.imie} {self.nazwisko}"


class Konsultacja(models.Model):
    lekarz = models.ForeignKey(Lekarz, on_delete=models.CASCADE, related_name='konsultacje_lekarza')
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE, related_name='konsultacje_pacjenta')
    opis_problemu = models.TextField(max_length=200)
    data_konsultacji = models.DateTimeField()
    zrealizowana = models.BooleanField(default=False)

    def __str__(self):
        return f"Opis problemu: {self.opis_problemu}"


class Plik(models.Model):
    konsultacja = models.ForeignKey(Konsultacja, on_delete=models.CASCADE, related_name='pliki')
    nadawca = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plik = models.FileField(upload_to='pliki_konsultacji/')
    data_wyslania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plik dla konsultacji {self.konsultacja.id} - {self.data_wyslania.strftime('%Y-%m-%d %H:%M')}"


