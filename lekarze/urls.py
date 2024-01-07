from django.urls import path
from . import views

urlpatterns = [
    path('profil/', views.profil_lekarza, name='profil_lekarza'),
    path('dodaj-konsultacje/', views.dodaj_konsultacje, name='dodaj_konsultacje'),
    path('edytuj-profil/', views.edytuj_profil_lekarza, name='edytuj_profil_lekarza'),
    path('konsultacja/<int:konsultacja_id>/', views.szczegoly_konsultacji, name='szczegoly_konsultacji'),
]
