import json

from constants import http_response as http
from controllers.admin_controller import (
    EmployeeRefreshController,
    EmployeeSigninController,
)
from controllers.article_controller import ArticleController, ArticlesController
from controllers.contact_controller import ContactController
from controllers.subscriber_controller import SubscriberController
from security import cors


def routes():
    routes = {
        "/article": ArticleController,
        "/articles": ArticlesController,
        "/contact": ContactController,
        "/signin": EmployeeSigninController,
        "/subscribe": SubscriberController,
        "/refresh": EmployeeRefreshController,
    }
    return routes


def router(request):
    if request.method == "OPTIONS":
        _handle_options_request(request)
    if request.path not in routes():
        return (
            json.dumps({"error": "Path {} not Found".format(request.path)}),
            404,
            http.DEFAULT_HEADERS,
        )

    route = routes()[request.path]
    controller = route()
    if request.method.lower() not in dir(controller):
        return http.METHOD_NOT_ALLOWED
    if request.method.upper() == "GET":
        response, status, headers = controller.get(request)
    elif request.method.upper() == "POST":
        response, status, headers = controller.post(request)
    else:
        return http.METHOD_NOT_ALLOWED

    cors_headers, _ = cors.write_headers(request.headers.get("origin"))
    headers.update(cors_headers)
    return response, status, headers


def _handle_options_request(request):
    headers, allowed = cors.write_headers(request.headers.get("origin"))
    if allowed:
        return ("", 204, headers)
    return ("", 403, headers)
