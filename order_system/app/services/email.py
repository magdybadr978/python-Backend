from flask_mail import Message
from app import mail
import threading

def send_async_email(app, msg):
    """Send email asynchronously to avoid blocking the main thread."""
    with app.app_context():
        mail.send(msg)

def send_confirmation_email(app, email, order):
    """Send an order confirmation email to the customer."""
    msg = Message(
        subject="Order Confirmation",
        sender=app.config["MAIL_DEFAULT_SENDER"],
        recipients=[email]
    )
    msg.body = f"Your order {order.id} for {order.quantity} items has been confirmed.\nTotal: ${order.total_price}"

  
    thread = threading.Thread(target=send_async_email, args=(app, msg))
    thread.start()
