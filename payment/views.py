from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from azampay import Azampay
from decouple import config

class MNOCheckout(APIView):
    def post(self, request):
        payment_data = request.data
        
# class MNOCheckoutTwo(APIView):
#     def get(self):
#         azampay = Azampay(
#             app_name=config('APP_NAME'),
#             client_id=config('CLIENT_ID'),
#             client_secret=config('CLIENT_SECRET'),
#             x_api_key=config('X_API_KEY'),
#             sandbox=True
#         )
#         checkout = azampay.mobile_checkout(
#             amount=10,
#             mobile='+255623470540',
#             provider='Halopesa',
#             external_id='1234569'
#         )
#         payment_link = azampay.generate_payment_link(amount=10, external_id='1234569', provider='Halopesa')['data']
        
#         return Response({'payment_link': payment_link, 'checkout': checkout}, status=status.HTTP_200_OK)