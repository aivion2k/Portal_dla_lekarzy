from django import forms
from .models import Konsultacja
from .models import Lekarz, Plik


class KonsultacjaForm(forms.ModelForm):
    class Meta:
        model = Konsultacja
        fields = ['pacjent', 'opis_problemu', 'data_konsultacji']
        widgets = {
            'data_konsultacji': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class EdytujProfilLekarzaForm(forms.ModelForm):
    class Meta:
        model = Lekarz
        fields = ['imie', 'nazwisko', 'specjalizacja', 'numer_pwz']  # Zaktualizuj zgodnie z modelem Lekarz


class WyszukajPacjentaForm(forms.Form):
    PESEL = forms.CharField(label='PESEL', max_length=11)


class PlikForm(forms.ModelForm):
    class Meta:
        model = Plik
        fields = ['plik']
