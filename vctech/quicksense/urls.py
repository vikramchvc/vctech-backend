from django.urls import path

from .views import SummariseAPI, PaymentAPI

urlpatterns = [
    path('api/summarise/', SummariseAPI.as_view(), name='summarise'),
    path('api/user/', SummariseAPI.as_view(), name='summarise'),
    path('api/payment', PaymentAPI.as_view(), name='payment')
]
