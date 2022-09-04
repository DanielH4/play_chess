# play_chess (Work in progress)
A Django backend that allows for the creation, storing, and manipulation of classic chess 
games via REST APIs and websockets.

# Table of Contents
1. [Getting Started](#getting-started)
2. [REST API](#rest-api)
3. [Websockets](#websockets)

## Getting Started

### Installation
```
pip install git+https://github.com/DanielH4/chesslib.git
pip install -r requirements.txt
```

### Running local server
```
python manage.py runserver 0.0.0.0:8000
```

## REST API

### Create Chess game
#### Request
`POST /chessgames/`
```
curl -X POST http://localhost:8000/chessgames/
```
#### Response
```
{"id":1,"turn":"white","in_check":false,"checkmate":false,"board":[{"type":"rook","color":"white","value":5,"has_moved":false},{"type":"knight","color":"white","value":3},{"type":"bishop","color":"white","value":3},{"type":"queen","color":"white","value":9},{"type":"king","color":"white","value":null,"has_moved":false},{"type":"bishop","color":"white","value":3},{"type":"knight","color":"white","value":3},{"type":"rook","color":"white","value":5,"has_moved":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"rook","color":"black","value":5,"has_moved":false},{"type":"knight","color":"black","value":3},{"type":"bishop","color":"black","value":3},{"type":"queen","color":"black","value":9},{"type":"king","color":"black","value":null,"has_moved":false},{"type":"bishop","color":"black","value":3},{"type":"knight","color":"black","value":3},{"type":"rook","color":"black","value":5,"has_moved":false}]}
```

### List Chess games
#### Request
`GET /chessgames/`
```
curl http://localhost:8000/chessgames/
```
#### Response
```
[{"id":1,"turn":"white","in_check":false,"checkmate":false,"board":[{"type":"rook","color":"white","value":5,"has_moved":false},{"type":"knight","color":"white","value":3},{"type":"bishop","color":"white","value":3},{"type":"queen","color":"white","value":9},{"type":"king","color":"white","value":null,"has_moved":false},{"type":"bishop","color":"white","value":3},{"type":"knight","color":"white","value":3},{"type":"rook","color":"white","value":5,"has_moved":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"rook","color":"black","value":5,"has_moved":false},{"type":"knight","color":"black","value":3},{"type":"bishop","color":"black","value":3},{"type":"queen","color":"black","value":9},{"type":"king","color":"black","value":null,"has_moved":false},{"type":"bishop","color":"black","value":3},{"type":"knight","color":"black","value":3},{"type":"rook","color":"black","value":5,"has_moved":false}]}]
```

### Chess game details
#### Request
`GET /chessgames/<id>/`
```
curl http://localhost:8000/chessgames/1/
```
#### Response
```
{"id":1,"turn":"white","in_check":false,"checkmate":false,"board":[{"type":"rook","color":"white","value":5,"has_moved":false},{"type":"knight","color":"white","value":3},{"type":"bishop","color":"white","value":3},{"type":"queen","color":"white","value":9},{"type":"king","color":"white","value":null,"has_moved":false},{"type":"bishop","color":"white","value":3},{"type":"knight","color":"white","value":3},{"type":"rook","color":"white","value":5,"has_moved":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"rook","color":"black","value":5,"has_moved":false},{"type":"knight","color":"black","value":3},{"type":"bishop","color":"black","value":3},{"type":"queen","color":"black","value":9},{"type":"king","color":"black","value":null,"has_moved":false},{"type":"bishop","color":"black","value":3},{"type":"knight","color":"black","value":3},{"type":"rook","color":"black","value":5,"has_moved":false}]}
```

### Delete game
#### Request
`DELETE /chessgames/<id>/`
```
curl -X DELETE http://localhost:8000/chessgames/2/
```

### Get legal moves
#### Request
`GET /chessgames/<id>/legal-moves/` 
```
curl http://localhost:8000/chessgames/1/legal-moves/
```
#### Response
```
{"legal_moves":[["g2","g4"],["b1","c3"],["g1","h3"],["c2","c4"],["a2","a3"],["b1","a3"],["a2","a4"],["d2","d3"],["e2","e4"],["h2","h4"],["e2","e3"],["f2","f4"],["d2","d4"],["c2","c3"],["h2","h3"],["b2","b3"],["f2","f3"],["b2","b4"],["g2","g3"],["g1","f3"]]}
```

### Get legal moves from specific square
#### Request
`GET /chessgames/<id>/legal-moves/<from>/`
```
curl http://localhost:8000/chessgames/1/legal-moves/a2/
```
#### Response
```
{"legal_moves":[["a2","a3"],["a2","a4"]]}
```

### Move a piece
#### Request
`POST /chessgames/<id>/move/<from>/<to>/` 
```
curl http://localhost:8000/chessgames/1/move/a2/a4/
```
#### Response
```
{"id":1,"turn":"black","in_check":false,"checkmate":false,"board":[{"type":"rook","color":"white","value":5,"has_moved":false},{"type":"knight","color":"white","value":3},{"type":"bishop","color":"white","value":3},{"type":"queen","color":"white","value":9},{"type":"king","color":"white","value":null,"has_moved":false},{"type":"bishop","color":"white","value":3},{"type":"knight","color":"white","value":3},{"type":"rook","color":"white","value":5,"has_moved":false},null,{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},{"type":"pawn","color":"white","value":1,"en_passantable":false},null,null,null,null,null,null,null,null,{"type":"pawn","color":"white","value":1,"en_passantable":true},null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"pawn","color":"black","value":1,"en_passantable":false},{"type":"rook","color":"black","value":5,"has_moved":false},{"type":"knight","color":"black","value":3},{"type":"bishop","color":"black","value":3},{"type":"queen","color":"black","value":9},{"type":"king","color":"black","value":null,"has_moved":false},{"type":"bishop","color":"black","value":3},{"type":"knight","color":"black","value":3},{"type":"rook","color":"black","value":5,"has_moved":false}]}
```

## Websockets
### Connect to a game
`wss://localhost:8000/ws/<id>/`
```
websocat ws://127.0.0.1:8000/ws/chessgames/1/
```

### Legal moves
#### Send
```
{"event":"legal-moves"}
```
or
```
{"event":"legal-moves","square":"d7"}
```
#### Receive
```
{"legal_moves": [["d7", "d6"], ["d7", "d5"]]}
```

### Move
#### Send
```
{"event":"move","from_square":"e7","to_square":"e6"}
```
#### Receive
```
{"id": 1, "turn": "white", "in_check": false, "checkmate": false, "board": [{"type": "rook", "color": "white", "value": 5, "has_moved": false}, {"type": "knight", "color": "white", "value": 3}, {"type": "bishop", "color": "white", "value": 3}, {"type": "queen", "color": "white", "value": 9}, {"type": "king", "color": "white", "value": null, "has_moved": false}, {"type": "bishop", "color": "white", "value": 3}, {"type": "knight", "color": "white", "value": 3}, {"type": "rook", "color": "white", "value": 5, "has_moved": false}, null, {"type": "pawn", "color": "white", "value": 1, "en_passantable": false}, {"type": "pawn", "color": "white", "value": 1, "en_passantable": false}, {"type": "pawn", "color": "white", "value": 1, "en_passantable": false}, {"type": "pawn", "color": "white", "value": 1, "en_passantable": false}, {"type": "pawn", "color": "white", "value": 1, "en_passantable": false}, {"type": "pawn", "color": "white", "value": 1, "en_passantable": false}, {"type": "pawn", "color": "white", "value": 1, "en_passantable": false}, null, null, null, null, null, null, null, null, {"type": "pawn", "color": "white", "value": 1, "en_passantable": true}, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, {"type": "pawn", "color": "black", "value": 1, "en_passantable": false}, null, null, null, {"type": "pawn", "color": "black", "value": 1, "en_passantable": false}, {"type": "pawn", "color": "black", "value": 1, "en_passantable": false}, {"type": "pawn", "color": "black", "value": 1, "en_passantable": false}, {"type": "pawn", "color": "black", "value": 1, "en_passantable": false}, null, {"type": "pawn", "color": "black", "value": 1, "en_passantable": false}, {"type": "pawn", "color": "black", "value": 1, "en_passantable": false}, {"type": "pawn", "color": "black", "value": 1, "en_passantable": false}, {"type": "rook", "color": "black", "value": 5, "has_moved": false}, {"type": "knight", "color": "black", "value": 3}, {"type": "bishop", "color": "black", "value": 3}, {"type": "queen", "color": "black", "value": 9}, {"type": "king", "color": "black", "value": null, "has_moved": false}, {"type": "bishop", "color": "black", "value": 3}, {"type": "knight", "color": "black", "value": 3}, {"type": "rook", "color": "black", "value": 5, "has_moved": false}]}
```
The updated game state is broadcast to all clients connected to the specific game.
