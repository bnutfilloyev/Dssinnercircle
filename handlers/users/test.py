import paypalrestsdk

from data.config import MODE, CLIEND_ID, CLIENT_SECRET

paypalrestsdk.configure({
    "mode": MODE,
    "client_id": CLIEND_ID,
    "client_secret": CLIENT_SECRET})


payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {"payment_method": "paypal"},
    "redirect_urls": {
        "return_url": f"http://t.me/",
        "cancel_url": f"http://t.me/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "item",
                "sku": "item",
                "price": f"100.00",
                "currency": "USD",
                "quantity": 1}]},
        "amount": {"total": f"100.00", "currency": "USD"},
        "description": "This is the payment transaction description."}]})

if payment.create():
    print('Success')
else:
    print('Error')

for link in payment.links:
    if link.rel == "approval_url":
        approval_url = str(link.href)
        token = approval_url.split('=')[-1]

print(payment.id)
print(payment.find())




# print(payment_history.payments)
# print(payment)
