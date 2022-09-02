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

        