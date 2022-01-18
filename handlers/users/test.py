# import stripe
#
# stripe.api_key = "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"
# amount = 1000
# currency = 'USD'
# bot_name = 'test'
#
# price = stripe.Price.create(
#     unit_amount=amount,
#     currency=currency.lower(),
#     product="prod_KyDBeasX5H30dU",
# )
#
# payment = stripe.checkout.Session.create(
#     success_url=f"http://t.me/{bot_name}",
#     cancel_url=f"http://t.me/{bot_name}",
#     line_items=[
#         {
#             "price": price.id,
#             "quantity": 1,
#         },
#     ],
#     mode="payment",
# )
#
# print(payment.url)
# #
# # import paypalrestsdk
# # import logging
# #
# # paypalrestsdk.configure({
# #   "mode": "live", # sandbox or live
# #   "client_id": "",
# #   "client_secret": "" })
# #
# # payment = paypalrestsdk.Payment({
# #     "intent": "sale",
# #     "payer": {
# #         "payment_method": "paypal"},
# #     "redirect_urls": {
# #         "return_url": "http://localhost:3000/payment/execute",
# #         "cancel_url": "http://localhost:3000/"},
# #     "transactions": [{
# #         "item_list": {
# #             "items": [{
# #                 "name": "item",
# #                 "sku": "item",
# #                 "price": "5.00",
# #                 "currency": "USD",
# #                 "quantity": 1}]},
# #         "amount": {
# #             "total": "5.00",
# #             "currency": "USD"},
# #         "description": "This is the payment transaction description."}]})
# #
# # if payment.create():
# #   print("Payment created successfully")
# # else:
# #   print(payment.error)