from flask import Blueprint, Response, current_app, request
import json

health = Blueprint('health', __name__)


@health.route("/health")
def check_health():
    return Response(response=json.dumps({
        "status": "OK",
        "headers": request.headers.to_list(),
        "commit": current_app.config["COMMIT"],
        "app": current_app.config["APP_NAME"]
    }), mimetype='application/json', status=200)
