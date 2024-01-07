from django.urls import path
from . import views

urlpatterns = [
    path('profil/', views.profil_pacjenta, name='profil_pacjenta'),
    path('edytuj-profil/', views.edytuj_profil_pacjenta, name='edytuj_profil_pacjenta')
]