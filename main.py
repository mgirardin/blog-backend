import json 
from constants import http_response
from security import cors
from controllers.ArticleController import ArticleController, ArticlesController
from controllers.AdminController import EmployeeSigninController, EmployeeRefreshController
from controllers.SubscriberController import SubscriberController
from controllers.ContactController import ContactController

def routes():
    routes = {
        "/article" : ArticleController,
        "/articles" : ArticlesController,
        "/contact": ContactController,
        "/signin": EmployeeSigninController,
        "/subscribe": SubscriberController,
        "/refresh": EmployeeRefreshController
    }
    return routes

def router(request):
    if request.method == 'OPTIONS':
        headers, allowed = cors.write_headers(request.headers.get("origin"))
        if(allowed):
            return ('', 204, headers)
        return ('', 403, headers)
    if(request.path not in routes()):
        return json.dumps({"error" : "Path {} not Found".format(request.path)}), 404, http_response.DEFAULT_HEADERS
    tmp_router = routes()[request.path]
    tmp_object = tmp_router()
    response = {}
    if(request.method.lower() not in dir(tmp_object)):
        return json.dumps({"error" : "MethodNotAllowed"}), 405, http_response.DEFAULT_HEADERS
    if(request.method.upper() == "GET"):
        response, status, headers = tmp_object.get(request)
    elif(request.method.upper() == "POST"):
        response, status, headers = tmp_object.post(request)
    else:
        return json.dumps({ "error" : "MethodNotAllowed"}), 405, http_response.DEFAULT_HEADERS
    cors_headers, _ = cors.write_headers(request.headers.get("origin"))
    headers.update(cors_headers)
    return response, status, headers