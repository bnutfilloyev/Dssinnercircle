

import stripe
stripe.api_key = 'sk_test_51KEZEsERl483ddfA3KEsZCD6lOy4YXGHtBCMMYaCZptJSxPzeFhiemobcWDLnFNmTwmTk5hdRfPr6MRJahBHBwh800e6JigWOW'
YOUR_DOMAIN = 'http://localhost:4242'

try:
  checkout_session = stripe.checkout.Session.create(
    line_items=[
      {
        'price': 'price_1KF2n6ERl483ddfAJCJuaaUq',
        'quantity': 1,
      },
    ],
    mode='payment',
    success_url=YOUR_DOMAIN + '/success.html',
    cancel_url=YOUR_DOMAIN + '/cancel.html',
  )
except Exception as e:
  print(e)

# print(checkout_session.url)