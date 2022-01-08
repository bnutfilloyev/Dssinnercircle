import paypalrestsdk

from data.config import MODE, CLIEND_ID, CLIENT_SECRET, CHANEL
from loader import bot

paypalrestsdk.configure({
    "mode": MODE,
    "client_id": CLIEND_ID,
    "client_secret": CLIENT_SECRET})

async def create_token_paypal(amount, bot_name):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "redirect_urls": {
            "return_url": f"http://t.me/{bot_name}",
            "cancel_url": f"http://t.me/{bot_name}"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "item",
                    "sku": "item",
                    "price": f"{amount}.00",
                    "currency": "USD",
                    "quantity": 1}]},
            "amount": {"total": f"{amount}.00", "currency": "USD"},
            "description": "This is the payment transaction description."}]})

    if payment.create():
        await bot.send_message(CHANEL, f"<code>{payment}</code>")
    else:
        await bot.send_message(CHANEL, str(payment.error))

    for link in payment.links:
        if link.rel == "approval_url":
            approval_url = str(link.href)
            token = approval_url.split('=')[-1]

    return token, payment.id

async def check_status_paypal(pay_id):
    payment_history = paypalrestsdk.Payment.all()
    payment_history.to_dict()
    payer_dict = []

    for i in payment_history.to_dict()['payments']:
        payer_dict.append(i['id'])

    return pay_id in payer_dict