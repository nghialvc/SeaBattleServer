from django.db import models
from django.conf import settings

# Create your models here.
class Room(models.Model):
    turn = models.IntegerField(default=1)
    port = models.IntegerField(default=8080)
    player1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='player2')
    move1 = models.IntegerField(default=-1)
    move2 = models.IntegerField(default=-1)
    map1 = models.CharField(default='', max_length=200)
    map2 = models.CharField(default='', max_length=200)
    result = models.IntegerField(default=0)
    status = models.CharField(default='Enable', max_length=200, null=True)

    def __str__(self):
        return "player "+str(self.player1.id)+" player"+str(self.player2.id) 
