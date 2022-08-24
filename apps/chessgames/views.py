from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.chessgames.models import ChessGame
from apps.chessgames.serializers import ChessGameSerializer


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
