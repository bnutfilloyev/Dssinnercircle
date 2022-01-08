import stripe

from data.config import STRIPE

stripe.api_key = STRIPE


async def create_link_stripe(amount, bot_name):
    price = stripe.Price.create(
        unit_amount=amount,
        currency="usd",
        product="prod_KusYEEi1WpoXKX",
    )

    payment = stripe.checkout.Session.create(
        success_url=f"http://t.me/{bot_name}",
        cancel_url=f"http://t.me/{bot_name}",
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            },
        ],
        mode="payment",
    )

    return [payment.url, payment.payment_intent]


async def check_status_stripe(intent_id):
    intent = stripe.PaymentIntent.retrieve(
        intent_id
    )
    return intent.status
