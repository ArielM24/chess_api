    
from dataclasses import asdict, dataclass


@dataclass
class Piece():
    name: str
    column: str
    row: int
    
    def __str__(self):
        return "{} {}".format(self.number, self.name)
    
    def to_map(self):
        return {'name': self.name, 'column': self.column, 'row': self.row}
    
    @staticmethod
    def initial_pieces() -> list:
        pieces = [
            Piece(name='White King',column='e',row=1),
            Piece(name='White Queen',column='d', row=1),
            Piece(name='White Bishop', column='f', row=1),
            Piece(name='White Bishop', column='c',row= 1),
            Piece(name='White Knight', column='g', row=1),
            Piece(name='White Knight', column='b', row=1),
            Piece(name='White Rook', column='h', row=1),
            Piece(name='White Rook', column='a', row=1),
            Piece(name='White Pawn', column='a', row=2),
            Piece(name='White Pawn', column='b', row=2),
            Piece(name='White Pawn', column='c', row=2),
            Piece(name='White Pawn', column='d', row=2),
            Piece(name='White Pawn', column='e', row=2),
            Piece(name='White Pawn', column='f', row=2),
            Piece(name='White Pawn', column='g', row=2),
            Piece(name='White Pawn', column='h', row=2),
            
            Piece(name='Black King',column='e',row=8),
            Piece(name='Black Queen', column='d', row=8),
            Piece(name='Black Bishop', column='f', row=8),
            Piece(name='Black Bishop', column='c',row= 8),
            Piece(name='Black Knight', column='g', row=8),
            Piece(name='Black Knight', column='b', row=8),
            Piece(name='Black Rook', column='h', row=8),
            Piece(name='Black Rook', column='a', row=8),
            Piece(name='Black Pawn', column='b', row=7),
            Piece(name='Black Pawn', column='c', row=7),
            Piece(name='Black Pawn', column='d', row=7),
            Piece(name='Black Pawn', column='e', row=7),
            Piece(name='Black Pawn', column='f', row=7),
            Piece(name='Black Pawn', column='g', row=7),
            Piece(name='Black Pawn', column='h', row=7),
        ]
        
        return [p.to_map() for p in pieces]