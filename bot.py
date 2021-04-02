import websocket

SOCKET= "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
      print('open_connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message ):
    print('recieved message')
    print(message)
ws = websocket.WebsocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()