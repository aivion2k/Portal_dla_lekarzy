from django.shortcuts import render, redirect
from .models import Konsultacja, Plik
from .forms import KonsultacjaForm  # Musisz utworzyć ten formularz
from .forms import EdytujProfilLekarzaForm  # Formularz, który trzeba stworzyć
from .forms import KonsultacjaForm, WyszukajPacjentaForm, PlikForm
from pacjenci.models import Pacjent
from django.shortcuts import render, get_object_or_404
from .models import Konsultacja
from komunikacja.models import Wiadomosc
from komunikacja.forms import WiadomoscForm  # Formularz do wysyłania wiadomości


def profil_lekarza(request):
    lekarz = request.user.lekarz
    konsultacje = Konsultacja.objects.filter(lekarz=request.user.lekarz, zrealizowana=False)
    return render(request, 'lekarze/profil.html', {'lekarz': lekarz, 'konsultacje': konsultacje})


def edytuj_profil_lekarza(request):
    lekarz = request.user.lekarz
    if request.method == 'POST':
        form = EdytujProfilLekarzaForm(request.POST, instance=lekarz)
        if form.is_valid():
            form.save()
            return redirect('profil_lekarza')
    else:
        form = EdytujProfilLekarzaForm(instance=lekarz)
    return render(request, 'lekarze/edytuj_profil.html', {'form': form})


def dodaj_konsultacje(request):
    search_form = WyszukajPacjentaForm(request.POST or None)
    konsultacja_form = None
    pacjent_znaleziony = False

    if search_form.is_valid():
        pesel = search_form.cleaned_data['pesel']
        try:
            pacjent = Pacjent.objects.get(pesel=pesel)
            pacjent_znaleziony = True
            konsultacja_form = KonsultacjaForm(initial={'pacjent': pacjent.id})
        except Pacjent.DoesNotExist:
            pacjent = None

    if 'add_konsultacja' in request.POST:
        konsultacja_form = KonsultacjaForm(request.POST)
        if konsultacja_form.is_valid():
            konsultacja = konsultacja_form.save(commit=False)
            konsultacja.lekarz = request.user.lekarz
            konsultacja.save()
            return redirect('profil_lekarza')

    return render(request, 'lekarze/dodaj_konsultacje.html', {
        'search_form': search_form,
        'konsultacja_form': konsultacja_form,
        'pacjent_znaleziony': pacjent_znaleziony
    })


def szczegoly_konsultacji(request, konsultacja_id):
    konsultacja = get_object_or_404(Konsultacja, pk=konsultacja_id)
    wiadomosci = Wiadomosc.objects.filter(konsultacja=konsultacja)
    pliki = Plik.objects.filter(konsultacja=konsultacja)
    wiadomosc_form = WiadomoscForm()
    plik_form = PlikForm()

    if request.method == 'POST':
        if 'submit_wiadomosc' in request.POST:
            wiadomosc_form = WiadomoscForm(request.POST)
            if wiadomosc_form.is_valid():
                print('Wiadomosc poprawna')
                wiadomosc = wiadomosc_form.save(commit=False)
                wiadomosc.konsultacja = konsultacja
                wiadomosc.nadawca = request.user
                wiadomosc.save()
                return redirect('szczegoly_konsultacji', konsultacja_id=konsultacja_id)  # Dodane przekierowanie
            else:
                print('Wiadomosc niepoprawna')

        elif 'usun_konsultacje' in request.POST:
            konsultacja.delete()
            return redirect('profil_lekarza')  # Przekieruj z powrotem do profilu lekarza

        elif 'submit_plik' in request.POST:
            plik_form = PlikForm(request.POST, request.FILES)
            if plik_form.is_valid():
                plik = plik_form.save(commit=False)
                plik.konsultacja = konsultacja
                plik.nadawca = request.user
                plik.save()
                return redirect('szczegoly_konsultacji', konsultacja_id=konsultacja_id)

    if request.method == 'POST' and 'zrealizuj_konsultacje' in request.POST:
        konsultacja.zrealizowana = True
        konsultacja.save()
        return redirect('profil_lekarza')  # Przekieruj z powrotem do profilu lekarza

    return render(request, 'lekarze/szczegoly_konsultacji.html', {
        'konsultacja': konsultacja,
        'wiadomosci': wiadomosci,
        'pliki': pliki,
        'wiadomosc_form': wiadomosc_form,
        'plik_form': plik_form
    })

