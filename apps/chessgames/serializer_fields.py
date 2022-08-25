from rest_framework import serializers

from chesslib.chess_board_utils import index_to_square


class LegalMoveListField(serializers.ListField):
    """
    A ListField that represents one legal move as a list of two squares, eg. [from, to].
    """
    choices = [index_to_square(i) for i in range(64)]
    child = serializers.ChoiceField(choices)
    allow_empty = False
    min_length = 2
    max_length = 2


class LegalMovesListField(serializers.ListField):
    """
    A ListField that represents a list of legal moves.
    """
    child = LegalMoveListField()
    allow_empty = True
