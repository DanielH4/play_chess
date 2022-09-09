from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from apps.chessgames.consumers import AnonymousChessGameConsumer


websocket_urlpatterns = format_suffix_patterns([
    path('ws/chessgames/anonymous/<int:game_id>/', AnonymousChessGameConsumer.as_asgi()),
])
