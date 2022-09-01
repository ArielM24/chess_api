from django.urls import path
from .views import *

urlpatterns = [
    path('home', HomeView.as_view()),
    path('new_game', NewGameView.as_view()),
    path('make_move', MakeMoveView.as_view()),
]