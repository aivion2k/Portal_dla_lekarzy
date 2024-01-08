from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User


class LekarzRegistrationForm(UserCreationForm):

    # Dodany komentarz
    numer_pwz = forms.CharField(max_length=7, min_length=7, help_text='Podaj ważny numer PWZ.')
    specjalizacja = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'numer_pwz', 'specjalizacja']


    def clean_numer_pwz(self):
        numer_pwz = self.cleaned_data.get('numer_pwz')

        # Sprawdzenie, czy numer PWZ nie zaczyna się od 0
        if numer_pwz.startswith('0'):
            raise ValidationError("Numer PWZ nie może zaczynać się od 0.")

        # Sprawdzenie cyfry kontrolnej
        wagi = [1, 2, 3, 4, 5, 6]
        suma = sum(int(cyfra) * waga for cyfra, waga in zip(numer_pwz[1:], wagi))
        cyfra_kontrolna = suma % 11

        if int(numer_pwz[0]) != cyfra_kontrolna:
            raise ValidationError("Nieprawidłowa cyfra kontrolna w numerze PWZ.")

        return numer_pwz


class PacjentRegistrationForm(UserCreationForm):
    pesel = forms.CharField(max_length=11)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'pesel']

