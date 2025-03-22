import logging
from flask import request, jsonify, Blueprint
from assistant.services.my_assistant import Assistant

api_bp = Blueprint('api', __name__)

@api_bp.route("/ask", methods=["POST"])
def ask():
    """
    Handle user chat requests.
    Expects JSON input with `user_input` containing `text_input` or `voice_input`.
    Returns an LLM-generated response.
    """
    visitor_input = request.json.get("visitor_input")

    try:
        response = Assistant.get_response(visitor_input)
        logging.info(f"Response generated: {response}")
        return jsonify({"response": response}), 200
    except Exception as e:
        logging.exception("Error generating chatbot response")
        return jsonify({"error": "An error occurred while generating a response."}), 500
