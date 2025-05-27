from flask import Blueprint, request, jsonify
from services.face_recognition import register_face

face_bp = Blueprint("face", __name__)

@face_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    result = register_face(data)
    return jsonify(result)