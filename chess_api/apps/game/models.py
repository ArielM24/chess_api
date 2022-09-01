import dataclasses
from djongo import models

from chess_api.apps.game.managers import GameManager

# Create your models here.

class Game(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    player_w_nick = models.TextField()
    player_w_code = models.TextField()
    player_b_nick = models.TextField()
    player_b_code = models.TextField()
    winner = models.TextField(default='none')
    time = models.DurationField(blank=True)
    board = models.JSONField(blank=True, null=True, default=list)
    moves = models.JSONField(blank=True, null=True, default=list)
    
    objects = GameManager()
    
    def __str__(self):
        return '{} {}'.format(self.id, self.winner)
    
    