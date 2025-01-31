from flask import current_app
from app import db
from app.models.order import Order
from app.models.product import Product
from app.services.stock import check_stock, update_stock
from app.services.payment import process_payment
from app.services.email import send_confirmation_email

def create_order(product_id, quantity, email, payment_method_id):
    """Handles full order processing: stock validation, payment, and confirmation."""
    
    if not check_stock(product_id, quantity):
        return {"error": "Not enough stock"}, 400

    product = Product.query.get(product_id)
    total_price = product.price * quantity

    order = Order(product_id=product_id, quantity=quantity, total_price=total_price, email=email)
    db.session.add(order)
    db.session.commit()

    # Process payment using real integration
    payment_result = process_payment(order.id, total_price, payment_method_id)

    if payment_result["success"]:
        order.status = "Paid"
        update_stock(product_id, quantity)
        db.session.commit()
        
        # Send confirmation email
        send_confirmation_email(current_app, email, order)
        
        return {"message": "Order placed successfully", "order_id": order.id, "payment_id": payment_result["payment_id"]}, 201
    else:
        order.status = "Failed"
        db.session.commit()
        return {"error": "Payment failed", "details": payment_result["error"]}, 400