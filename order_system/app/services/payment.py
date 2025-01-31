import os
import stripe
from dotenv import load_dotenv

load_dotenv()  

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def process_payment(order_id, amount, payment_method_id):
    """Process payment using a real payment gateway (Stripe)."""
    try:
      
        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Convert dollars to cents
            currency="usd",
            payment_method=payment_method_id,
            confirm=True  # Automatically confirm the payment
        )

        # If payment succeeds, return True
        return {"success": True, "payment_id": payment_intent.id}

    except stripe.error.StripeError as e:
        # Log the error and return failure
        return {"success": False, "error": str(e)}
