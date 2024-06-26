#!/usr/bin/python3
from os import getenv

from flask import Flask, jsonify
from flask_cors import CORS

from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, origins=["0.0.0.0"])
host = getenv("HBNB_API_HOST", "0.0.0.0")
port = getenv("HBNB_API_PORT", "5000")


@app.teardown_appcontext
def teardown(exception):
    """
    Teardown function for the Flask 
    application context.
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404 status code.
    Returns a JSON response with the message 
    "Not found" and a status code of 404.
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host, port, threaded=True, debug=True)
