import os
import json
import constants.http_response
from dal import Contact
from security.recaptcha import handle_captcha_token

class ContactController(object):
    def post(self, request):
        payload = request.get_json()
        needed_parameters = ["first_name", "last_name", "email", "number", "message", "recaptcha"]
        if(not all(elem in payload for elem in needed_parameters)):
            return MISSING_PARAMETER
        recaptcha = payload["recaptcha"]
        recaptcha_score = handle_captcha_token(recaptcha)
        if(recaptcha_score<0.4):
            return json.dumps({"status": "error", "error" : "CaptchaNotAllowed"}),200,DEFAULT_HEADERS
        first_name = payload["first_name"]
        last_name = payload["last_name"]
        email = payload["email"]
        number = payload["number"]
        message = payload["message"]
        email = payload["email"]
        try:
            Contact.create(first_name, last_name, email, number, message)
        except Exception as e:
            print(e)
        return json.dumps({"status": "ok"}), 200, DEFAULT_HEADERS