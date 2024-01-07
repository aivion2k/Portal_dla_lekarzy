from django import forms
from .models import Pacjent


class EdytujProfilPacjentaForm(forms.ModelForm):
    class Meta:
        model = Pacjent
        fields = ['imie', 'nazwisko']  # Zaktualizuj zgodnie z modelem Lekarz