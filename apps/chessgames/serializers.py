from rest_framework import serializers

from apps.chessgames.models import ChessGame
from apps.chessgames.serializer_fields import *


class ChessGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessGame
        fields = '__all__'


class LegalMovesSerializer(serializers.Serializer):
    legal_moves = LegalMovesListField()
