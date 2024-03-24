from accounts.models import UserModel
from .models import SummarizerModel
from .constants import Constants
from vctech import logger


class CreditHandler():

    def isAllowed(user: UserModel):
        summarizerObjs = SummarizerModel.objects.filter(user=user)
        if (summarizerObjs != None and len(summarizerObjs) > 0):
            credit = summarizerObjs[0].credit
            if (credit != 0):
                return True
        return False

    def getSumarizerObj(user: UserModel):
        summarizerObjs = SummarizerModel.objects.filter(user=user)
        if (summarizerObjs != None and len(summarizerObjs) > 0):
            return summarizerObjs[0]
        return None

    def updateCredit(email, plan):
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

    def resolvePlanCredit(userObj: UserModel, plan):
        if (plan == Constants.MONTHLY_PLAN):
            userObj.credit = Constants.MONTHLY_PLAN_CREDIT
        if (plan == Constants.YEARLY_PLAN):
            userObj.credit = Constants.YEARLY_PLAN_CREDIT
