from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .creditshandler import CreditHandler
from .summarizehandler import SummarizerHandler
from .paymenthandler import PaymentHandler
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json


class SummariseAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        summarizerObj = CreditHandler.getSumarizerObj(user)
        response = {
            "user": user.email,
            "credit": summarizerObj.credit,
            "plan": summarizerObj.plan
        }
        return Response(response)

    def post(self, request):
        return SummarizerHandler.execute(request)


class PaymentAPI(APIView):
    def post(self, request):
        json_data = json.loads(request.body.decode('utf-8'))
        email = json_data["email"]
        plan = json_data["plan"]
        CreditHandler.updatePlan(email, plan)

        response = {"credit", "exhausted"}
        return Response(response)


@csrf_exempt
@require_POST
def PaymentGateWay(request):
    try:
        PaymentHandler.execute(request)
        return JsonResponse({'message': 'Data received successfully'}, status=200)
    except:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    


@csrf_exempt
def SummarizeGateWay(request):
    if request.method == 'POST':
        return JsonResponse({'message': 'Data received successfully'}, status=200)
    else:
        
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
