from djongo import models

# Create your models here.

class Piece(models.Model):
    name = models.CharField(max_length=15)
    number = models.IntegerField()
    column = models.CharField(max_length=2)
    row = models.IntegerField()
    
    def __str__(self):
        return "{} {}".format(self.number, self.name)
    
    def initial_pieces(self) -> list:
        return [
            {'White King', 1, 'e', 1}
        ]