from .auth_routes import auth_routes

def register_auth_routes(app):
    app.register_blueprint(auth_routes, url_prefix="/auth")
