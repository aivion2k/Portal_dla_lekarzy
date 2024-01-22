from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User


class LekarzRegistrationForm(UserCreationForm):

    numer_pwz = forms.CharField(max_length=7, min_length=7)
    specjalizacja = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'numer_pwz', 'specjalizacja']


    def clean_numer_pwz(self):
        numer_pwz = self.cleaned_data.get('numer_pwz')

        if numer_pwz.startswith('0'):  # Sprawdzenie 0 na początku
            raise ValidationError("PWZ nie może zaczynać się od 0.")

        # Cyfry kontrolnej
        waga = [1, 2, 3, 4, 5, 6]
        suma = sum(int(cyfra) * waga for cyfra, waga in zip(numer_pwz[1:], waga))
        cyfra_kontr = suma % 11

        if int(numer_pwz[0]) != cyfra_kontr:
            raise ValidationError("Niewłaściwa cyfra kontrolna w numerze PWZ.")

        return numer_pwz


class PacjentRegistrationForm(UserCreationForm):
    PESEL = forms.CharField(max_length=11)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'PESEL']

