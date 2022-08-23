import json

from django.db import models

from chesslib.api import Chess


class ChessGame(models.Model):
    Color = models.TextChoices('Color', 'white black')
    turn = models.CharField(choices=Color.choices, max_length=5)
    in_check = models.BooleanField()
    checkmate = models.BooleanField()
    board = models.JSONField()

    @classmethod
    def create_default_game(cls):
        game = Chess()

        return cls(
            turn=game.turn,
            in_check=game.in_check,
            checkmate=game.checkmate,
            board = json.loads(game.toJSON()).get('board').get('board')
        )
