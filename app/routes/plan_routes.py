from flask import Blueprint, request, jsonify
from app.controllers.user_plans import create_user_plan, find_user_plans, add_to_cart, verify_payment
from app.models.user_plans import UserPlan


user_id = "123"

plan_bp = Blueprint("plan", __name__)


@plan_bp.route("/create", methods=["POST"])
def create():
    data = {
        **request.json,
        "user_id": user_id,
    }
    _, _ = create_user_plan(data)
    return jsonify({"message": "User Plan created"}), 201


@plan_bp.route("/", methods=["GET"])
def find_user_plan():
    filters = request.json
    user_plans = [
        UserPlan(**user_plan).model_dump() for user_plan in find_user_plans(filters)
    ]
    return jsonify({"data": user_plans}), 200


@plan_bp.route("/<plan_id>/add_to_cart", methods=["PUT"])
def checkout(plan_id: str):
    response = add_to_cart(plan_id)
    return jsonify({"data": "Plan Added Successfully" if response else "ERROR"}), 200


@plan_bp.route("/<plan_id>/verify_payment", methods=["PUT"])
def payment(plan_id):
    response = verify_payment(plan_id)
    return jsonify({"data": "Payment Verified" if response else "ERROR in Payment"}), 200
