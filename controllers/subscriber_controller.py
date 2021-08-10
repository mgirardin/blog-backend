import json

from constants import http_response
from dal.subscriber_dao import SubscriberDao
from messages.subscriber import Subscriber
from security.recaptcha import handle_captcha_token


class SubscriberController(object):
    def post(self, request):
        payload = request.get_json()
        needed_parameters = ["email", "recaptcha"]
        if(not all(elem in payload for elem in needed_parameters)):
            return http_response.MISSING_PARAMETER
        recaptcha = payload["recaptcha"]
        recaptcha_score = handle_captcha_token(recaptcha)
        if(recaptcha_score<0.4):
            return json.dumps({"status": "error", "error" : "CaptchaNotAllowed"}), 200, http_response.DEFAULT_HEADERS
        email = payload["email"]
        try:
            subscriber = Subscriber(email)
            SubscriberDao.create(subscriber)
        except Exception as e:
            print(e)
            return json.dumps({"status": "error"}), 500, http_response.DEFAULT_HEADERS
        return json.dumps({"status": "ok"}), 200, http_response.DEFAULT_HEADERS

