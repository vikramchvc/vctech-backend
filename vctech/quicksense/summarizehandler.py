import json
from .creditshandler import CreditHandler
from .summarizerService import Summarizer
# from .wordPresshandler import WordPressHandler
from .models import YoutubeModel
from rest_framework.response import Response
from .responses import ErrorResponse, SucessResponse, Errors
from .constants import Constants


class SummarizerHandler():

    def newSummary(summariser: Summarizer):
        response = summariser.summarise()
        if (response == Errors.NO_TRANSCRIPT):
            return ErrorResponse.NO_TRANSCRIPT
        YoutubeModel(youtubeId=id, json_data=json.dumps(response)).save()

    def execute(request):
        user = request.user
        json_data = json.loads(request.body.decode('utf-8'))
        summariser = Summarizer(json_data["video_id"], json_data["link"])
        determinant = CreditHandler.isAllowed(user, summariser)
        if (determinant == SucessResponse.ALLOWED_TO_SUMARIZE_CODE):
            try:
                id = json_data["video_id"]
                youtubeIDs = YoutubeModel.objects.filter(youtubeId=id)
                if (youtubeIDs != None and len(youtubeIDs) > 0):
                    youtubeID = youtubeIDs[0]
                    # response = WordPressHandler.getContent(youtubeID.youtubeId)
                    response = json.loads(youtubeID.json_data)
                    if (response == Constants.EMPTY_JSON):
                        return SummarizerHandler.newSummary(summariser)
                    return Response(response)
                else:
                    return SummarizerHandler.newSummary(summariser)
            except:
                return ErrorResponse.CANNOT_SUMMARIZE

        elif (determinant == ErrorResponse.LOW_CREDITS):
            return ErrorResponse.LOW_CREDITS
        else:
            return ErrorResponse.CREDITS_EXHAUSTED
