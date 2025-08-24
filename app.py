# app.py

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random, threading, time

app = Flask(__name__)
socketio = SocketIO(app)

# Track connected users: sid -> {username, avatar}
users: dict[str, dict] = {}

# In-memory store of temp messages for TTL cleanup (optional)
temp_messages: list[tuple[float, dict]] = []
TEMP_TTL = 10  # seconds

def cleanup_temp(interval: float = 5.0):
    """Background thread to purge old temporary messages."""
    while True:
        now = time.time()
        temp_messages[:] = [(t,p) for t,p in temp_messages if now - t < TEMP_TTL]
        time.sleep(interval)

# Start the cleanup thread
threading.Thread(target=cleanup_temp, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    # 1) Assign a random username + avatar
    username = f"User_{random.randint(1000,9999)}"
    gender   = random.choice(['girl','boy'])
    avatar   = f"https://avatar.iran.liara.run/public/{gender}?username={username}"
    users[request.sid] = {'username': username, 'avatar': avatar}

    # 2) Notify everyone that a new user joined
    emit('user_joined',
         {'username': username},
         broadcast=True)

    # 3) Send this client their own username & avatar
    emit('set_username',
         {'sid': request.sid, 'username': username, 'avatar': avatar},
         room=request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    # Remove them & notify everyone
    user = users.pop(request.sid, None)
    if user:
        emit('user_left',
             {'username': user['username']},
             broadcast=True)

@socketio.on('send_message')
def handle_message(data):
    # Broadcast a new message, marking temp if requested
    user = users.get(request.sid)
    if not user:
        return

    msg     = data.get('message', '')
    is_temp = bool(data.get('temp', False))
    payload = {
        'from_sid':      request.sid,
        'from_username': user['username'],
        'avatar':        user['avatar'],
        'message':       msg,
        'temp':          is_temp
    }

    if is_temp:
        # keep in temp_messages so server‐side could purge if needed
        temp_messages.append((time.time(), payload))

    emit('new_message', payload, broadcast=True)

@socketio.on('update_username')
def handle_update_username(data):
    old = users[request.sid]['username']
    new = data.get('username','').strip()
    if new and new != old:
        users[request.sid]['username'] = new
        emit('username_updated',
             {'old_username': old, 'new_username': new},
             broadcast=True)

if __name__ == '__main__':
    # Run on port 5050 (or change as you like)
    socketio.run(app, host='0.0.0.0', port=5050)
