import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from chess_api.apps.game.models import Game
from .serializers import *
# Create your views here.

class HomeView(APIView):
    def get(self, request):
        return Response(data={"Welcome to chess"})
    
    
class GetGameView(APIView):
    def get(self, request):
        print(request.query_params)
        data = GetGameSerializer(data=request.query_params)
        if data.is_valid():
            try:
                game = Game.objects.find_game(data.validated_data['game_id'])
                if game is not None:
                    js = GameSerializer(game).data
                    return Response(data={'game':js})
                return Response(data={'error':'game not found'})
            except Exception as e:
                return Response(data={'error':str(e)})
                
        return Response(data={'error':data.errors})
        
            
    
class NewGameView(APIView):
    def post(self, request):
        data = NewGameSerializer(data=request.data)
        
        if data.is_valid():
            print(data.validated_data)
            
            game = Game.objects.new_game(
                player_b_nick=data.validated_data['player_b_nick'],
                player_b_code=data.validated_data['player_b_code'],
                player_w_nick=data.validated_data['player_w_nick'],
                player_w_code=data.validated_data['player_w_code'],
            )
            if game is not None:
                return Response(data={'game_id':str(game._id)})
            else:
                return Response(data={'error':'something went wrong'})
        else:
            return Response(data={'error':data.errors})
        
class MakeMoveView(APIView):
    def post(self, request):
        data=MakeMoveSerializer(data=request.data)
        if data.is_valid():
            print(data.validated_data)
            success, game = Game.objects.make_move(move_data=data.validated_data)
            js = GameSerializer(game).data
            return Response(data={'success':success, 'game':js})
        else:
            return Response(data={'error':data.errors})
        
class JoinPlayerView(APIView):
    def post(self, request):
        data=JoinPlayerSerializer(data=request.data)
        if data.is_valid():
            pass
        else:
            return Response(data={'error':data.errors})