import json
from constants import http_response
from dal.contact_dao import ContactDao
from messages.contact import Contact
from security.recaptcha import handle_captcha_token

class ContactController(object):
    def post(self, request):
        payload = request.get_json()
        needed_parameters = ["first_name", "last_name", "email", "number", "message", "recaptcha"]
        if(not all(elem in payload for elem in needed_parameters)):
            return http_response.MISSING_PARAMETER
        recaptcha = payload["recaptcha"]
        recaptcha_score = handle_captcha_token(recaptcha)
        if(recaptcha_score<0.4):
            return json.dumps({"status": "error", "error" : "CaptchaNotAllowed"}), 200, http_response.DEFAULT_HEADERS
        first_name: str= payload["first_name"] 
        last_name: str = payload["last_name"]
        email: str = payload["email"]
        number: str = payload["number"]
        message: str = payload["message"]
        email: str = payload["email"]
        try:
            contact = Contact(first_name, last_name, email, number, message)
            ContactDao.create(contact)
        except Exception as e:
            print(e)
        return json.dumps({"status": "ok"}), 200, http_response.DEFAULT_HEADERS