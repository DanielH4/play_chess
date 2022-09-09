from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from apps.chessgames.views import (
    AnonymousChessGameViewSet,
    ChessGameViewSet,
)


chessgame_list = ChessGameViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
chessgame_detail = ChessGameViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})
chessgame_move = ChessGameViewSet.as_view({
    'post': 'move'
})
chessgame_legal_moves = ChessGameViewSet.as_view({
    'get': 'legal_moves'
})
anon_chessgame_list = AnonymousChessGameViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
anon_chessgame_detail = AnonymousChessGameViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})

urlpatterns = format_suffix_patterns([
    path('chessgames/', chessgame_list),
    path('chessgames/<int:pk>/', chessgame_detail),
    path('chessgames/<int:pk>/legal-moves/', chessgame_legal_moves),
    path('chessgames/<int:pk>/legal-moves/<str:square>/', chessgame_legal_moves),
    path('chessgames/<int:pk>/move/<str:from_square>/<str:to_square>/', chessgame_move),
    path('chessgames/anonymous/', anon_chessgame_list),
    path('chessgames/anonymous/<int:pk>/', anon_chessgame_detail),
])
