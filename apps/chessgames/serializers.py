from rest_framework import serializers
from apps.chessgames.models import ChessGame


class ChessGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChessGame
        exclude = ['id']
