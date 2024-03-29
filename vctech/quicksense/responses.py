from rest_framework.response import Response


class ErrorResponse():
    CREDITS_EXHAUSTED_CODE = 1001
    CREDITS_EXHAUSTED = Response(
        {"code": CREDITS_EXHAUSTED_CODE, "message": "Credits exhausted"})

    LOW_CREDITS_CODE = 1002
    LOW_CREDITS = Response(
        {"code": LOW_CREDITS_CODE, "message": "You dont have sufficient credits"})

    CANNOT_SUMMARIZE_CODE = 1003
    CANNOT_SUMMARIZE = Response(
        {"code": CANNOT_SUMMARIZE_CODE, "message": "Sorry unable to process your request"})

    NO_TRANSCRIPT_CODE = 1003
    NO_TRANSCRIPT = Response(
        {"code": NO_TRANSCRIPT_CODE, "message": "No summary found. Check for different video!"})


class SucessResponse():
    ALLOWED_TO_SUMARIZE_CODE = 2001


class Errors():
    NO_TRANSCRIPT = 3001
