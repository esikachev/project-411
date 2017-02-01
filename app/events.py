from flask_socketio import emit

from app import socketio
from bot import response


@socketio.on('message')
def handle_message(message):
    emit('message', response())
    print('received message: ' + str(message))
