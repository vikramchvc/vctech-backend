import hmac
import hashlib
import json
from .creditshandler import CreditHandler


class PaymentHandler():
    def split_signature(sig_header):
        timestamp, signature = sig_header.split(";")
        return timestamp.split("=")[1], signature.split("=")[1]


    def generate_hmac(timestamp, raw_body):
        payload = f"{timestamp}:".encode('utf-8') + raw_body
        secret_key = "pdl_ntfset_01ht4e3054eayjtzfjzgsw01bs_F87BO8TgBJs5/gXEvuYxHFIjrPC/C6Wh".encode('utf-8')
        return hmac.new(secret_key, msg=payload,digestmod=hashlib.sha256).hexdigest()


    def verify_signature(sig, raw_body):
        timestamp, paddle_signature = PaymentHandler.split_signature(sig)
        our_signature = PaymentHandler.generate_hmac(timestamp, raw_body)
        print(paddle_signature, our_signature)
        if paddle_signature != our_signature:
            return False
        else:
            return True  

    def execute(request):
        if(PaymentHandler.verify_signature()):
            json_data = json.loads(request.body.decode('utf-8'))
            print("Vc Debug=======================> ")
            print(json_data)
            print("===============================> ")
            # CreditHandler.updatePlan(email, plan)
            print("To do execute payment")
        else:
            print("dent execute payment")