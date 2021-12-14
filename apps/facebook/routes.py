from re import I
from flask import jsonify
from apps import db
from .models import Results
from apps.facebook import facebook_blueprint

@facebook_blueprint.route("/get_results",methods=["GET"])
def get_results():
    try:
        pass
    except Exception as e:
        return jsonify(str(e))