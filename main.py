import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
# async_mode='eventlet' ensures the right server is used
socketio = SocketIO(app, async_mode='eventlet')

@app.route("/chatbot")
def chatbot():
    return render_template("chat2.0.html")

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('message')
def handle_message(data):
    print(f"Received: {data}")
    socketio.send(data)

if __name__ == '__main__':
    # This is used for local development
    socketio.run(app)
