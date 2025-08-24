# Client-Server Chat Application

A real-time chat application built with Flask and WebSocket technology that enables instant messaging between multiple users with features like temporary messages, user management, and real-time updates.

## 🚀 Features

- **Real-time Messaging**: Instant message delivery using WebSocket connections
- **User Management**: Automatic random username and avatar assignment
- **Temporary Messages**: Messages with configurable TTL (Time To Live)
- **Real-time Updates**: Live notifications for user joins, leaves, and username changes
- **Avatar System**: Dynamic avatar generation using external avatar service
- **Session Management**: Automatic cleanup of expired temporary messages

## 🛠️ Tech Stack

### Backend
- **Flask** (3.1.0) - Python web framework
- **Flask-SocketIO** (5.5.1) - WebSocket support for Flask
- **Eventlet** (0.39.1) - Asynchronous networking library
- **Python 3.13** - Programming language

### Frontend
- **HTML5** - Markup language
- **CSS3** - Styling
- **JavaScript** - Client-side functionality
- **Socket.IO Client** - WebSocket client library

### Architecture
- **Client-Server Model** - Traditional web architecture
- **WebSocket Protocol** - Full-duplex communication
- **In-Memory Storage** - User sessions and temporary messages
- **Background Threading** - Automatic cleanup processes

## 📁 Project Structure

```
Client-Server-Chat-Application/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── activate.sh           # Virtual environment activation script
├── app.log              # Application logs
├── templates/            # HTML templates
│   └── index.html       # Main chat interface
└── venv/                # Python virtual environment
```

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone git@github.com:J3l3l/Client-Server-Chat-Application-.git
   cd Client-Server-Chat-Application-
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

   Or use the activation script:
   ```bash
   chmod +x activate.sh
   ./activate.sh
   python app.py
   ```

### Access the Application

- **Local URL**: http://localhost:5050
- **Network URL**: http://0.0.0.0:5050

## 🔧 Configuration

### Environment Variables
- **Port**: Default is 5050 (configurable in `app.py`)
- **Host**: Default is 0.0.0.0 (accessible from any network interface)

### Customization
- **Temporary Message TTL**: Modify `TEMP_TTL` variable in `app.py` (default: 10 seconds)
- **Cleanup Interval**: Modify the `cleanup_temp` function interval (default: 5 seconds)
- **Avatar Service**: Change the avatar URL in the `handle_connect` function

## 📱 Usage

1. **Open the application** in your web browser
2. **Automatic Assignment**: You'll be assigned a random username and avatar
3. **Start Chatting**: Type messages in the input field and press Enter
4. **Temporary Messages**: Check the "temp" option for messages that auto-delete
5. **Update Username**: Use the username update feature to personalize your identity

## 🔌 API Endpoints

### WebSocket Events
- `connect` - User connects to the chat
- `disconnect` - User leaves the chat
- `send_message` - Send a new message
- `update_username` - Update user's username

### HTTP Routes
- `GET /` - Main chat interface

## 🧹 Maintenance

### Logs
- Application logs are stored in `app.log`
- Monitor for errors and user activity

### Cleanup
- Temporary messages are automatically cleaned up every 5 seconds
- Expired messages (older than 10 seconds) are removed from memory

## 👨‍💻 Author

**Jalal** - [GitHub Profile](https://github.com/J3l3l)

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- Socket.IO for WebSocket implementation
- Avatar service providers for dynamic avatar generation

---

**Note**: This is a development/demo application. For production use, consider implementing proper authentication, database persistence, and security measures.
