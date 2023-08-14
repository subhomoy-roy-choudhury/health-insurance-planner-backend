from flask import Blueprint, request, jsonify
# from app.models.user import UserCreate, UserUpdate
# from app.controllers.user_controller import create_user

plan_bp = Blueprint('plan', __name__)

@plan_bp.route('/create', methods=['POST'])
def create():
    return jsonify({'message': 'User created'}), 201