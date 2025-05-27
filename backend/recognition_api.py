from flask import Flask, request, jsonify
import base64
import numpy as np
import cv2
import mediapipe as mp
from db import save_face_encoding

app = Flask(__name__)
mp_face_mesh = mp.solutions.face_mesh

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    image_data = base64.b64decode(data['image'])
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        results = face_mesh.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if not results.multi_face_landmarks:
            return jsonify({"error": "No face detected"}), 400

        # Use landmarks as embeddings (placeholder logic)
        landmarks = results.multi_face_landmarks[0]
        encoding = []
        for point in landmarks.landmark:
            encoding.extend([point.x, point.y, point.z])
        
        save_face_encoding(data['name'], encoding)
        return jsonify({"message": "Face registered using MediaPipe!"})

if __name__ == '__main__':
    app.run(port=5000)
