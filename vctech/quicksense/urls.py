from django.urls import path

from .views import SummariseAPI, PaymentAPI, SummarizeGateWay, PaymentGateWay

urlpatterns = [
    path('api/insight/summarise/', SummariseAPI.as_view(), name='summarise'),
    path('api/user/', SummariseAPI.as_view(), name='summarise'),
    path('api/payment', PaymentAPI.as_view(), name='payment'),
    path('api/sumarise/', SummarizeGateWay, name='your_endpoint'),
    path('haduenhy/payment/', PaymentGateWay, name='your_endpoint')
]
