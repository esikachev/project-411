from app import socketio


@socketio.on('message')
def handle_message(message):
    print('received message: ' + str(message))