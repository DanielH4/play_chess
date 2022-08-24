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
        """
        Returns an instance created from a default Chess object.
        """
        game = Chess()

        return cls(
            turn=game.turn,
            in_check=game.in_check,
            checkmate=game.checkmate,
            board=json.loads(game.toJSON()).get('board').get('board')
        )

    def to_chess(self):
        """
        Returns a Chess object created from instance.
        """
        data = {
            'turn': self.turn,
            'in_check': self.in_check,
            'checkmate': self.checkmate,
            'board': {'board': self.board}
        }
        chess_json_str = json.dumps(data)

        return Chess.fromJSON(chess_json_str)

    @classmethod
    def from_chess(cls, chess):
        """
        Returns an instance created from given Chess object.
        """
        return cls(
            turn=chess.turn,
            in_check=chess.in_check,
            checkmate=chess.checkmate,
            board=json.loads(chess.toJSON()).get('board').get('board')
        )
