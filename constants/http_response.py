import json

DEFAULT_HEADERS = {"content-type": "application/json"}

DEFAULT_RESPONSE = json.dumps({"status": "success"}), 200, DEFAULT_HEADERS
METHOD_NOT_ALLOWED = (json.dumps({"error": "MethodNotAllowed"}), 405, DEFAULT_HEADERS)
PERMISSION_DENIED = (
    json.dumps({"status": "error", "error": "PermissionDenied"}),
    401,
    DEFAULT_HEADERS,
)
NOT_AUTHORIZED = (
    json.dumps({"status": "error", "error": "WrongCredentials"}),
    401,
    DEFAULT_HEADERS,
)
MISSING_PARAMETER = (
    json.dumps({"status": "error", "error": "MissingParameter"}),
    401,
    DEFAULT_HEADERS,
)
