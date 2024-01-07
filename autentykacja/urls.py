from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/lekarz/', views.register_as_lekarz, name='register_as_lekarz'),
    path('register/pacjent/', views.register_as_pacjent, name='register_as_pacjent'),
]
