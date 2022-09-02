from djongo import models
from .data_classes import Piece
from bson import ObjectId

class GameManager(models.DjongoManager):
    def find_game(self, game_id):
        return self.filter(_id=ObjectId(game_id)).first()
    
    def new_game(self, player_w_code='', player_w_nick='',
                 player_b_nick='', player_b_code=''):
        game = self.create(
            player_b_nick=player_b_nick,
            player_b_code=player_b_code,
            player_w_nick=player_w_nick,
            player_w_code=player_w_code,
            board=Piece.initial_pieces()
        )
        return game
    
    def make_move(self, move_data):
        game = self.find_game(move_data['game_id'])
        if game is not None:
            if not self.move_piece(game, move_data):
                return False, None
            move_coords = '{}{}-{}{}'.format(
                    move_data['current_column'],
                    move_data['current_row'],
                    move_data['next_column'],
                    move_data['next_row'],
                )
            if move_data['is_player_w']:
                game.moves.append(move_coords)
            else:
                game.moves[move_data['move_number']] += ' ' + move_coords
            game.save()
            return True, game
        return False, None
    
    def move_piece(self,game, move_data):
        try:
            piece_to_move = self.find_piece(
                game, move_data['current_column'], move_data['current_row'])
            piece_to_eat = self.find_piece(
                game, move_data['next_column'], move_data['next_row'])
            
            print(piece_to_move, piece_to_eat)
            
            if piece_to_eat is not None:
                game.board[game.board.index(piece_to_eat)]['row'] = -1
                game.board[game.board.index(piece_to_eat)]['column'] = ''
            
            game.board[game.board.index(piece_to_move)]['row'] = move_data['next_row']
            game.board[game.board.index(piece_to_move)]['column'] = move_data['next_column']
            game.save()
            return True
        except:
            return False
        
    def find_piece(self,game, column, row):
        return next((p for p in game.board if p['column'] == column
                      and p['row'] == row), None)
        
    def join_player(self, player_info):
        game = self.find_game(player_info['game_id'])
        joined = False
        if player_info['player_type'] == 'player_b':
            joined = self._join_player_b(game, player_info)
        elif player_info['player_type'] == 'player_w':
            joined = self._join_player_w(game, player_info)
        elif player_info['player_type'] == 'spectator':
            joined = True
        if joined:
            return self.find_game(player_info['game_id'])
            
        
    def _join_player_b(self, game, player_info):
        if game.player_b_code != '':
            if game.player_b_code == player_info['player_code']:
                return True
        else:
            game.player_b_code = player_info['player_code']
            game.player_b_nick = player_info['player_nick']
            game.save()
            return True
        return False
    
    def _join_player_w(self, game, player_info):
        if game.player_w_code != '':
            if game.player_w_code == player_info['player_code']:
                return True
        else:
            game.player_w_code = player_info['player_code']
            game.player_w_nick = player_info['player_nick']
            game.save()
            return True
        return False
    
    def set_winner(self, winner_data):
        game = self.find_game(winner_data['game_id'])
        if game is not None:
            game.winner = winner_data['winner']
            game.save()
            return game