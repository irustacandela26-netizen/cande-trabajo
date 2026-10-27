from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='trivia_inicio'),
    path('pregunta1/', views.pregunta1, name='trivia_pregunta1'),
    path('pregunta2/', views.pregunta2, name='trivia_pregunta2'),
    path('pregunta3/', views.pregunta3, name='trivia_pregunta3'),
    path('pregunta4/', views.pregunta4, name='trivia_pregunta4'),
    path('game-over/', views.game_over, name='trivia_game_over'),
    path('win/', views.win, name='trivia_win'),
]
