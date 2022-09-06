from rest_framework import serializers

from chess_api.apps.game.models import Game

class GameSerializer(serializers.ModelSerializer):
    board = serializers.SerializerMethodField()
    moves = serializers.SerializerMethodField()
    
    class Meta:
        model = Game
        #fields = '__all__'
        exclude = ('player_w_code', 'player_b_code')
        
    def get_board(self, obj):
        return list(map(lambda x: dict(x), obj.board))
    
    def get_moves(self, obj):
        return list(obj.moves)
    
class IdGameSerializer(serializers.Serializer):
    game_id = serializers.CharField(required=True)
    
 
class NewGameSerializer(serializers.Serializer):
    player_w_nick = serializers.CharField(default="")
    player_w_code = serializers.CharField(default="")
    player_b_nick = serializers.CharField(default="")
    player_b_code = serializers.CharField(default="")
    
class JoinPlayerSerializer(serializers.Serializer):
    player_nick = serializers.CharField(required=True)
    player_code = serializers.CharField(required=True)
    player_type = serializers.CharField(required=True)
    game_id = serializers.CharField(required=True)
    
class MakeMoveSerializer(serializers.Serializer):
    current_row = serializers.IntegerField(required=True)
    current_column = serializers.CharField(required=True)
    next_row = serializers.IntegerField(required=True)
    next_column = serializers.CharField(required=True)
    is_player_w = serializers.BooleanField(required=True)
    move_number = serializers.IntegerField(required=True)
    game_id = serializers.CharField(required=True)
    
class SetWinnerSerializer(serializers.Serializer):
    winner = serializers.CharField(required=True)
    game_id = serializers.CharField(required=True)