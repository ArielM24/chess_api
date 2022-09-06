from django.urls import path
from .views import *

urlpatterns = [
    path('home', HomeView.as_view()),
    path('get_game', GetGameView.as_view()),
    path('new_game', NewGameView.as_view()),
    path('make_move', MakeMoveView.as_view()),
    path('join_player', JoinPlayerView.as_view()),
    path('set_winner', SetWinnerView.as_view()),
    path('get_moved_piece', GetMovedPieceView.as_view()),
]