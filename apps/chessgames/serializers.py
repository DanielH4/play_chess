from rest_framework import serializers

from apps.chessgames.models import AnonymousChessGame, ChessGame
from apps.chessgames.serializer_fields import *


class AnonymousChessGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousChessGame
        exclude = ['white_player', 'black_player']


class ChessGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessGame
        fields = '__all__'


class LegalMovesSerializer(serializers.Serializer):
    legal_moves = LegalMovesListField()
