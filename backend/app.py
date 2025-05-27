from flask import Flask
from api.face_routes import face_bp
from api.chat_routes import chat_bp

app = Flask(__name__)
app.register_blueprint(face_bp, url_prefix="/face")
app.register_blueprint(chat_bp, url_prefix="/chat")

if __name__ == '__main__':
    app.run(debug=True)