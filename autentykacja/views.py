from .forms import LekarzRegistrationForm, PacjentRegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from lekarze.models import Lekarz
from pacjenci.models import Pacjent


def register_as_lekarz(request):
    if request.method == 'POST':
        form = LekarzRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.jest_lekarzem = True
            user.save()
            Lekarz.objects.create(user=user, specjalizacja=form.cleaned_data['specjalizacja'], numer_pwz=form.cleaned_data['numer_pwz'])
            return redirect('home')
    else:
        form = LekarzRegistrationForm()
    return render(request, 'autentykacja/register.html', {'form': form})

def register_as_pacjent(request):
    if request.method == 'POST':
        form = PacjentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.jest_pacjentem = True
            user.save()
            Pacjent.objects.create(user=user, PESEL=form.cleaned_data['PESEL'])
            return redirect('home')
    else:
        form = PacjentRegistrationForm()
    return render(request, 'autentykacja/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Możesz dodać wiadomość o błędzie
            pass
    return render(request, 'autentykacja/login.html')
