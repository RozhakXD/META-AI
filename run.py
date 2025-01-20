from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from engine.routes import chat_bp
from flask_cors import CORS

app = Flask(__name__, template_folder='engine/templates')
CORS(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "META AI Chat API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(chat_bp)

if __name__ == '__main__':
    app.run(debug=True)