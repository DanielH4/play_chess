import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from apps.chessgames.models import AnonymousChessGame
from apps.chessgames.serializers import AnonymousChessGameSerializer, LegalMovesSerializer


class AnonymousChessGameConsumer(JsonWebsocketConsumer):
    def get_chessgame_instance(self):
        return AnonymousChessGame.objects.get(id=self.game_id)

    def get_session_key(self):
        return self.scope['session'].session_key

    def connect(self):
        """
        Accepts a connection call and creates/joins a channel layer group.
        """
        self.accept()

        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.group_name = f"game_{self.game_id}"
        self.clean_up = True
        chessgame_instance = self.get_chessgame_instance()

        if chessgame_instance.is_full():
            self.clean_up = False
            self.send_json({'error':'Game is full.'})
            self.close()

        session = self.scope['session']
        session.create()
        chessgame_instance.add_player(self.get_session_key())

        # join group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

    def disconnect(self, close_code):
        """
        Discards the assigned channel layer group and deletes AnonymousChessGame instance upon disconnect.
        """
        if self.clean_up:
            self.get_chessgame_instance().delete()

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
        chessgame_instance = self.get_chessgame_instance()

        is_player_turn = chessgame_instance.is_player_turn(self.get_session_key())
        if not is_player_turn:
            return

        # Example text_data: {"event":"move","from_square":"e7","to_square":"e6"}
        if event == 'move':
            chessgame_instance.move(data['from_square'], data['to_square'])
            serializer = AnonymousChessGameSerializer(chessgame_instance)

            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type': 'move',
                    'data': serializer.data
                }
            )

        # Example text_data: {"event":"legal-moves","square":"d2"}
        elif event == 'legal-moves':
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
