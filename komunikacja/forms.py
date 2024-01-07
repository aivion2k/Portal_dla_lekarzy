from django import forms
from .models import Wiadomosc

class WiadomoscForm(forms.ModelForm):
    tresc = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 40,
            'style': 'resize:none;',
            'placeholder': 'Wpisz tutaj wiadomość...'
        }),
        label='',  # Usuwa etykietę "Treść"
    )

    class Meta:
        model = Wiadomosc
        fields = ['tresc']


