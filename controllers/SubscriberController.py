import os
import json
import http_response
from dal import Subscriber
from security.recaptcha import handle_captcha_token

class SubscriberController(object):
    def post(self, request):
        payload = request.get_json()
        needed_parameters = ["email", "recaptcha"]
        if(not all(elem in payload for elem in needed_parameters)):
            return MISSING_PARAMETER
        recaptcha = payload["recaptcha"]
        recaptcha_score = handle_captcha_token(recaptcha)
        if(recaptcha_score<0.4):
            return json.dumps({"status": "error", "error" : "CaptchaNotAllowed"}),200,DEFAULT_HEADERS
        email = payload["email"]
        try:
            Subscriber.create(email)
        except Exception as e:
            print(e)
            return json.dumps({"status": "error"}), 500, DEFAULT_HEADERS
        return json.dumps({"status": "ok"}), 200, DEFAULT_HEADERS

