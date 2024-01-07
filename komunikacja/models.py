from django.db import models
from django.conf import settings
from lekarze.models import Konsultacja  # Zaimportuj model Konsultacja z aplikacji lekarze

class Wiadomosc(models.Model):
    konsultacja = models.ForeignKey(Konsultacja, on_delete=models.CASCADE, related_name='wiadomosci')
    nadawca = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tresc = models.TextField(verbose_name="Treść")
    data_wyslania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wiadomość od {self.nadawca} - {self.data_wyslania.strftime('%Y-%m-%d %H:%M')}"
