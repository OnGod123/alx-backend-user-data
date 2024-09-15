#!/usr/bin/env python3
"""
Route module for the API
"""

from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from api.v1.views import app_views
from api.v1.auth.auth import Auth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize auth variable
auth = None

# Determine authentication type from environment variable
auth_type = getenv('AUTH_TYPE')

if auth_type == 'auth':
    auth = Auth()

elif auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()
@app.errorhandler(404)
def not_found(error) -> str:
    """
    Handles 404 Not Found errors.
    """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """
    Handles 401 Unauthorized errors.
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden_error(error) -> str:
    """
    Handles 403 Forbidden errors.
    """
    return jsonify({"error": "Forbidden"}), 403

@app.before_request
def before_request():
    """
    Filters requests before they are processed. Checks if the request requires authentication
    and verifies the authorization header and current user.
    """
    if auth is None:
        return
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

    if auth.require_auth(request.path, excluded_paths):
        if auth.authorization_header(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
