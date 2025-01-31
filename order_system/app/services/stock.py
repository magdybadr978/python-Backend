from app.models.product import Product
from app import db

def check_stock(product_id, quantity):
    """Check if stock is available for a given product."""
    product = Product.query.get(product_id)
    return product and product.stock >= quantity

def update_stock(product_id, quantity):
    """Update stock after a successful order."""
    product = Product.query.get(product_id)
    if product:
        product.stock -= quantity
        db.session.commit()
