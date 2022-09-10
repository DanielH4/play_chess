import json

from django.db import models
from django.contrib.sessions.models import Session

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

    def move(self, from_square, to_square):
        """
        Perform a move on the chessboard and update instance.
        """
        chess = self.to_chess()
        chess.move(from_square, to_square)
        after_move = ChessGame.from_chess(chess)

        self.turn = after_move.turn
        self.in_check = after_move.in_check
        self.checkmate = after_move.checkmate
        self.board = after_move.board
        self.save()

    def legal_moves(self, square=None):
        """
        Returns the legal moves of the player in turn.
        If a square is specified, only returns legal moves from that square.
        """
        chess = self.to_chess()
        legal_moves = chess.legal_moves()

        # only consider legal moves originating from specified square
        if square is not None:
            legal_moves = filter(lambda move: move[0] == square, legal_moves)

        return legal_moves

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


class AnonymousChessGame(ChessGame):
    white_player = models.OneToOneField(Session,
                                        on_delete=models.CASCADE,
                                        default=None,
                                        null=True,
                                        blank=True,
                                        related_name='white_player')
    black_player = models.OneToOneField(Session,
                                        on_delete=models.CASCADE,
                                        default=None,
                                        null=True,
                                        blank=True,
                                        related_name='black_player')

    def is_full(self):
        return (self.white_player is not None and
                self.black_player is not None)

    def add_player(self, session_key):
        session = Session.objects.get(pk=session_key)

        if self.white_player is None:
            self.white_player = session
        elif self.black_player is None:
            self.black_player = session
        self.save()

    def is_player_turn(self, session_key):
        return any([self.turn == 'white' and session_key == self.white_player.session_key,
                    self.turn == 'black' and session_key == self.black_player.session_key])
