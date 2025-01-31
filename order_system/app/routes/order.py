from flask import Blueprint, request, jsonify
from app.services.order import create_order

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/", methods=["POST"])
def place_order():
    """Handles order placement and payment."""
    data = request.get_json()
    
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    email = data.get("email")
    payment_method_id = data.get("payment_method_id")

    if not all([product_id, quantity, email, payment_method_id]):
        return jsonify({"error": "Missing required fields"}), 400

    result = create_order(product_id, quantity, email, payment_method_id)
    return jsonify(result)
