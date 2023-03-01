import stripe
import os
from flask import Flask, request

stripe.api_key = os.environ.get('SECRET_KEY')

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = request.json

    if event['type'] == 'payment_intent.succeeded':
        pass
    elif event['type'] == 'payment_intent.failed':
        pass

    return {'success': True}

@app.route('/charge', methods=['POST'])
def charge():
    customer_id = request.form['customer_id']
    amount = request.form['amount']

    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency='usd',
        customer=customer_id
    )

    charge = stripe.PaymentIntent.confirm(
        intent.id,
        payment_method=intent.payment_method
    )

    if charge.status == 'succeeded':
        pass
    else:
        pass

    return {'success': True}