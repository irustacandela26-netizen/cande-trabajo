from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.escena, name='historia_escena'),
]

urlpatterns = [
    path('', views.inicio, name='historia_inicio'),
    path('isla/', views.isla, name='historia_isla'),
    path('tesoro/', views.tesoro, name='historia_tesoro'),
    path('final-bueno/', views.final_bueno, name='historia_final_bueno'),
    path('final-malo/', views.final_malo, name='historia_final_malo'),
    path('bosque/', views.bosque, name='historia_bosque'),
    path('torre/', views.torre, name='historia_torre'),
]
