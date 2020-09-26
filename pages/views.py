from django.shortcuts import render

import stripe
stripe.api_key = 'sk_test_51HQlYBKVWRemJMNbYdPyEEGInMoFLN9MwF1UA0m6rxk8o97VVB4jS5B4LXBjNN8XGeVXWiBjcNTT1NqIin9I1HJj00LtxiIU4C'
YOUR_DOMAIN = 'http://localhost:8000'
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def checkout_view(request, *args, **kwargs):
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {

                    'price_data': {

                        'currency': 'usd',

                        'unit_amount': 2000,

                        'product_data': {

                            'name': 'Stubborn Attachments',

                            'images': ['https://i.imgur.com/EHyR2nP.png'],

                        },

                    },

                    'quantity': 1,

                },

            ],

            mode='payment',

            success_url=YOUR_DOMAIN + '/success.html',

            cancel_url=YOUR_DOMAIN + '/cancel.html',

        );



    return render(request, "checkout.html", {'id': checkout_session.id})
