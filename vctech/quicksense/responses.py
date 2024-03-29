from rest_framework.response import Response
class ErrorResponse():
    CREDITS_EXHAUSTED_CODE = 1001
    CREDITS_EXHAUSTED = Response({"code":CREDITS_EXHAUSTED_CODE,"message":"Credits exhausted"})
    LOW_CREDITS_CODE = 1002
    LOW_CREDITS= Response({"code":LOW_CREDITS_CODE,"message":"You dont have sufficient credits"})

class SucessResponse():
    ALLOWED_TO_SUMARIZE_CODE = 2001
    
