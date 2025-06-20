from flask import Blueprint, request, jsonify
from fya.auth.api.dto import RegisterRequest, LoginRequest
from fya.auth.service.services.auth_service import AuthService

auth_routes = Blueprint("auth_routes", __name__)
service = AuthService()

@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    request_dto = RegisterRequest(**data)
    token = service.register(request_dto)
    return jsonify(token.__dict__), 201

@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    request_dto = LoginRequest(**data)
    token = service.login(request_dto)
    return jsonify(token.__dict__), 200
