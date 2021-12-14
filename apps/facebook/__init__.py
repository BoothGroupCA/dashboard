from flask import Blueprint

facebook_blueprint = Blueprint(
    'facebook_blueprint',
    __name__,
    url_prefix=''
)
