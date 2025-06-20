from flask import Flask
from fya.auth.service.routes import register_auth_routes

def create_app():
    app = Flask(__name__)
    register_auth_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
