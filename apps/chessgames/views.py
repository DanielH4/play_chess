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
        instance = self.get_object()
        chess = instance.to_chess()

        # handle invalid move
        if chess.move(from_square, to_square) is None:
            return Response(data={'message': 'Invalid move.'}, status=status.HTTP_400_BAD_REQUEST)

        updated_instance = ChessGame.from_chess(chess)
        updated_instance_serializer = ChessGameSerializer(updated_instance)
        serializer = ChessGameSerializer(instance, data=updated_instance_serializer.data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

    @action(methods=['get'],
            detail=True)
    def legal_moves(self, request, square=None,*args, **kwargs):
        """
        Returns instance's legal moves.
        """
        instance = self.get_object()
        chess = instance.to_chess()
        legal_moves = chess.legal_moves()

        if square is not None:
            legal_moves = filter(lambda move: move[0] == square, legal_moves)

        data = { 'legal_moves': legal_moves }
        serializer = LegalMovesSerializer(data=data)

        assert serializer.is_valid()
        return Response(serializer.data)
