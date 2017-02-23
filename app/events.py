from flask_socketio import emit

from app import socketio
from bot import get_response


@socketio.on('status')
def handle_message(message):
    # emit('message', 'Hello.')
    print('received status: ' + str(message))


@socketio.on('message')
def handle_message(message):
    emit('message', get_response(message))
    print('received message: ' + str(message))
