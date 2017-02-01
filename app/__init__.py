from flask import Flask
from flask_socketio import SocketIO

from app import routs, events

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
