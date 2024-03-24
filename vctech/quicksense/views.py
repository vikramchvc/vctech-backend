from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SummarizerModel, YoutubeModel
from .creditshandler import CreditHandler
from .summarizerService import Summarizer
from .wordPresshandler import WordPressHandler
import json


class SummariseAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        summarizerObj = CreditHandler.getSumarizerObj(user)
        response = {
            "user": user.email,
            "credit": summarizerObj.credit,
            "remaining_credit": 30,
            "plan": summarizerObj.plan
        }
        return Response(response)

    def post(self, request):
        user = request.user
        response = {"credit", "exhausted"}
        if (CreditHandler.isAllowed(user=user)):
            json_data = json.loads(request.body.decode('utf-8'))
            print("Vc check", json_data)
            summariser = Summarizer(json_data["video_id"], json_data["link"])
            id = json_data["video_id"]
            youtubeIDs = YoutubeModel.objects.filter(youtubeId=id)
            if (youtubeIDs != None and len(youtubeIDs) > 0):
                youtubeID = youtubeIDs[0]
                response = WordPressHandler.getContent(youtubeID.youtubeId)
            else:

                response = summariser.summarise()
                WordPressHandler.createContent(response, id)
                YoutubeModel(youtubeId=id).save()
        return Response(response)


class PaymentAPI(APIView):
    def get(self, request):
        print("Vc check"+str(request))

        response = {"credit", "exhausted"}
        return Response(response)

    def post(self, request):
        print("Vc check"+str(request))

        json_data = json.loads(request.body.decode('utf-8'))
        email = json_data["email"]
        plan = json_data["plan"]
        CreditHandler.updateCredit(email, plan)

        response = {"credit", "exhausted"}
        return Response(response)
