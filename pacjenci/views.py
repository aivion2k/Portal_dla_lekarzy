from django.shortcuts import render, redirect
from .models import Pacjent
from lekarze.models import Konsultacja
from .forms import EdytujProfilPacjentaForm

def profil_pacjenta(request):
    pacjent = Pacjent.objects.get(user=request.user)
    konsultacje = Konsultacja.objects.filter(pacjent=pacjent, zrealizowana=False)
    return render(request, 'pacjenci/profil.html', {'pacjent': pacjent, 'konsultacje': konsultacje})


def edytuj_profil_pacjenta(request):
    pacjent = request.user.pacjent
    if request.method == 'POST':
        form = EdytujProfilPacjentaForm(request.POST, instance=pacjent)
        if form.is_valid():
            form.save()
            return redirect('profil_pacjenta')
    else:
        form = EdytujProfilPacjentaForm(instance=pacjent)
    return render(request, 'pacjenci/edytuj_profil.html', {'form': form})