import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from apps.chessgames.models import ChessGame
from apps.chessgames.serializers import ChessGameSerializer, LegalMovesSerializer


class ChessGameConsumer(JsonWebsocketConsumer):
    def connect(self):
        """
        Accepts a connection call and creates/joins a channel layer group.
        """
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.group_name = f"game_{self.game_id}"

        # join group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        """
        Discards the assigned channel layer group and deletes ChessGame instance upon disconnect.
        """
        chessgame_instance = ChessGame.objects.get(id=self.game_id)
        chessgame_instance.delete()

        # discard group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive_json(self, data):
        """
        Handles events such as player move or getting legal moves.
        Broadcasts updated chess states to channel layer group.
        """
        event = data['event']

        # Example text_data: {"event":"move","from_square":"e7","to_square":"e6"}
        if event == 'move':
            chessgame_instance = ChessGame.objects.get(id=self.game_id)
            chessgame_instance.move(data['from_square'], data['to_square'])
            serializer = ChessGameSerializer(chessgame_instance)

            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'move',
                    'data': serializer.data
                }
            )

        # Example text_data: {"event":"legal-moves","square":"d2"}
        elif event == 'legal-moves':
            chessgame_instance = ChessGame.objects.get(id=self.game_id)

            square = None
            if 'square' in data:
                square = data['square']

            data = { 'legal_moves': chessgame_instance.legal_moves(square) }
            serializer = LegalMovesSerializer(data=data)

            assert serializer.is_valid()
            self.send_json(serializer.data)

    def move(self, event):
        """
        Event handler.
        """
        self.send_json(event['data'])
