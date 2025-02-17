import requests
from decouple import config

def get_access_token():
    url = 'https://authenticator.azampay.co.tz/AppRegistration/GenerateToken'
    headers = {'Content-Type': 'application/json'}
    data = {
        'appName': config('APP_NAME'),
        'clientId': config('CLIENT_ID'),
        'clientSecret': config('CLIENT_SECRET')
    }
    response = requests.post(url, headers=headers, json=data)
    response = response.json()
    return response['data']['accessToken']

def mno_checkout(payment_data):
    url = 'https://checkout.azampay.co.tz/azampay/mno/checkout'
    token = get_access_token()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    data = {
        'accountNumber': payment_data.phone_number,
        'amount': str(payment_data.amount),
        'currency': payment_data.currency,
        'externalId': str(payment_data.id),
        'provider': payment_data.provider,
        'additionalProperties': {}
    }
    response = requests.post(url, headers=headers, json=data)
    response = response.json()
    return response