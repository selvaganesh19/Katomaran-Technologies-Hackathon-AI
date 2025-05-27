from flask import Blueprint, request, jsonify
from services.rag_pipeline import run_rag_pipeline

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("question")
    result = run_rag_pipeline(user_input)
    return jsonify({"response": result})
