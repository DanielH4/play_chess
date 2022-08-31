from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from apps.chessgames.consumers import ChessGameConsumer


websocket_urlpatterns = format_suffix_patterns([
    path('ws/chessgames/<int:game_id>/', ChessGameConsumer.as_asgi()),
])
