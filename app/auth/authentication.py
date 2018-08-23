# Authentication class

from flask import request, jsonify, Blueprint
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from app.validation import FieldValidation
from app.models import User
from app.db.dbFunctions import is_user_exist, add_new_user, get_user_by_username

validate = FieldValidation()
auth_blueprint = Blueprint("auth_blueprint", __name__)

class RegisterUser(MethodView):
    # register new user
    def post(self):
        reg_info = request.get_json()

        userName = reg_info.get("username").strip()
        email    = reg_info.get("email").strip()
        password = reg_info.get("password")

        validation_resp = validate.client_validation(userName, password)

        if validation_resp:
            return validation_resp

        email_validation = validate.validate_email(email)

        if email_validation == False:
            return jsonify({"message": "wrong email entered, Please try again"}), 400

        if is_user_exist:
            return jsonify({"message": "User already exists"}), 400
        else:
            add_new_user(userName=userName, email=email, password=password)
            new_user = User(userName, email, password)
            return jsonify({"New User Created": new_user.__dict__}), 200


class Login(MethodView):
    def post(self):
        login_info = request.get_json()

        userName = login_info.get("username").strip()
        password = login_info.get("password").strip()

        login_validation = validate.client_validation(userName, password)

        if login_validation:
            return login_validation

        user_token = {}
        user = get_user_by_username(userName)

        if user:
            access_token = create_access_token(identity= userName)
            user_token["token"] = access_token
            return jsonify(user_token), 200

        return jsonify({"message": "user does not exit, register and login again"}), 404

registration_view = RegisterUser.as_view("registration_view")
login_view = Login.as_view("login_view")

auth_blueprint.add_url_rule("/api/auth/register",view_func=registration_view, methods=["POST"])
auth_blueprint.add_url_rule("/api/auth/login",view_func=login_view, methods=["POST"])



