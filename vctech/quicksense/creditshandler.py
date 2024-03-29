from accounts.models import UserModel
from .models import SummarizerModel
from .constants import Constants
from .summarizerService import Summarizer
from .responses import ErrorResponse,SucessResponse

class CreditHandler():
        
    def isAllowed(user: UserModel,summariser:Summarizer):
        summarizerObjs = SummarizerModel.objects.filter(user=user)
        userObj = summarizerObjs[0]
        credit = userObj.credit
        _,duration = summariser.getTransScript()
        if(credit<duration):
            return ErrorResponse.LOW_CREDITS_CODE
        CreditHandler.updateCredit(credit-duration,userObj)
        return SucessResponse.ALLOWED_TO_SUMARIZE_CODE

    def getSumarizerObj(user: UserModel):
        summarizerObjs = SummarizerModel.objects.filter(user=user)
        if (summarizerObjs != None and len(summarizerObjs) > 0):
            return summarizerObjs[0]
        return None

    def updatePlan(email, plan):
        user = UserModel.objects.filter(email=email)
        print("=========================VC debug================================")
        print(str(user))

        if (user != None and len(user) > 0):
            summarizerObjs = SummarizerModel.objects.filter(user=user[0])
            print(str(summarizerObjs))
            print("=========================VC debug================================")
            if (summarizerObjs != None and len(summarizerObjs) > 0):
                userObj = summarizerObjs[0]
                userObj.plan = plan
                CreditHandler.resolvePlanCredit(userObj, plan)
                userObj.save()
        return None
    
    def updateCredit(credit,user:SummarizerModel):
        user.credit = credit
        user.save()
        return None

    def resolvePlanCredit(userObj: UserModel, plan):
        if (plan == Constants.MONTHLY_PLAN):
            userObj.credit = Constants.MONTHLY_PLAN_CREDIT
        if (plan == Constants.YEARLY_PLAN):
            userObj.credit = Constants.YEARLY_PLAN_CREDIT
