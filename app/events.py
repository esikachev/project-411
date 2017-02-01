from flask_socketio import emit

from app import socketio
from bot import response


@socketio.on('status')
def handle_message(message):
    emit('message', 'Hello.')
    print('received status: ' + str(message))


@socketio.on('message')
def handle_message(message):
    emit('message', response())
    print('received message: ' + str(message))