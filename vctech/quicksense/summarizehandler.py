import json
from .creditshandler import CreditHandler
from .summarizerService import Summarizer
from .wordPresshandler import WordPressHandler
from .models import YoutubeModel
from rest_framework.response import Response
from .responses import ErrorResponse,SucessResponse

class SummarizerHandler():

    def execute(request):
        user = request.user
        json_data = json.loads(request.body.decode('utf-8'))
        summariser = Summarizer(json_data["video_id"], json_data["link"])
        determinant = CreditHandler.isAllowed(user,summariser)
        if (determinant==SucessResponse.ALLOWED_TO_SUMARIZE_CODE):
            id = json_data["video_id"]
            youtubeIDs = YoutubeModel.objects.filter(youtubeId=id)
            if (youtubeIDs != None and len(youtubeIDs) > 0):
                youtubeID = youtubeIDs[0]
                response = WordPressHandler.getContent(youtubeID.youtubeId)
                return Response(response)
            else:
                response = summariser.summarise()
                WordPressHandler.createContent(response, id)
                YoutubeModel(youtubeId=id).save()
                return Response(response)
            
        elif(determinant==ErrorResponse.LOW_CREDITS):
            return ErrorResponse.LOW_CREDITS
        else:
            return ErrorResponse.CREDITS_EXHAUSTED

                
        


