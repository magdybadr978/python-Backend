from flask import Blueprint, request, jsonify
from app import db
from app.models.product import Product


products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["GET"])
def get_products():
    """Get all available products."""
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "stock": p.stock, "price": p.price} for p in products])

@products_bp.route("/", methods=["POST"])
def add_product():
    """Add a new product to inventory."""
    data = request.json
    new_product = Product(name=data["name"], stock=data["stock"], price=data["price"])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added successfully", "id": new_product.id}), 201
