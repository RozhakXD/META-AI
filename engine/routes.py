from flask import Blueprint, request, jsonify, render_template, Response
from engine.utils import get_response_from_meta_ai

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/', methods=['GET'])
def index() -> str:
    return render_template('index.html')

@chat_bp.route('/api/chat', methods=['POST'])
def chat() -> Response:
    try:
        if request.content_type != 'application/json':
            return jsonify(
                {
                    'error': 'Content-Type must be application/json'
                }
            ), 415
        try:
            user_message = request.json.get('message', '')
        except Exception:
            return jsonify(
                {
                    'error': 'Invalid JSON body',
                }
            ), 400
        if not user_message:
            return jsonify(
                {
                    'error': 'No message provided'
                }
            ), 400
        meta_ai_response = get_response_from_meta_ai(user_message)
        if not meta_ai_response:
            return jsonify(
                {
                    'error': 'No response provided'
                }
            ), 500
        return jsonify(
            {
                'message': meta_ai_response
            }
        ), 200
    except Exception:
        return jsonify(
            {
                'error': 'An error occurred'
            }
        ), 500