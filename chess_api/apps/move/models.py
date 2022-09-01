from djongo import models

# Create your models here.

class Move(models.Model):
    _id = models.ObjectIdField(primary_key=True, db_column='_id')
    piece_number = models.IntegerField()
    
    current_row = models.CharField(max_length=2)
    current_column = models.IntegerField()
    
    next_row = models.CharField(max_length=2)
    next_column = models.IntegerField()
    
    def __str__(self):
        return '{}{}-{}{}'.format(self.current_column, self.current_row,
                                  self.next_column, self.next_row)