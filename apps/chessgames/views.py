from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.chessgames.models import ChessGame
from apps.chessgames.serializers import ChessGameSerializer, LegalMovesSerializer


class ChessGameViewSet(viewsets.ModelViewSet):
    queryset = ChessGame.objects.all()
    serializer_class = ChessGameSerializer

    @action(methods=['post'],
            detail=True)
    def move(self, request, from_square, to_square, *args, **kwargs):
        """
        Performs a legal move and updates instance.
        """
        chessgame_instance = self.get_object()
        chessgame_instance.move(from_square, to_square)
        serializer = ChessGameSerializer(chessgame_instance)

        return Response(serializer.data)

    @action(methods=['get'],
            detail=True)
    def legal_moves(self, request, square=None,*args, **kwargs):
        """
        Returns instance's legal moves.
        """
        chessgame_instance = self.get_object()

        data = { 'legal_moves': chessgame_instance.legal_moves(square=square) }
        serializer = LegalMovesSerializer(data=data)

        assert serializer.is_valid()
        return Response(serializer.data)
