# Authentication class

from flask import request, jsonify, Blueprint
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from app.validation import FieldValidation
from app.models import User
from app.db.dbFunctions import is_user_exist, add_new_user, get_user_by_username, is_email_exist
from flasgger import swag_from

validate = FieldValidation()
auth_blueprint = Blueprint("auth_blueprint", __name__)

class RegisterUser(MethodView):
    # register new user
    @swag_from("/.app/docs/register.yml")
    def post(self):
        reg_info = request.get_json()

        search_keys = ("username", "email", "password")

        if all(key in reg_info.keys() for key in search_keys):
            user_name = reg_info.get("username").strip()
            email    = reg_info.get("email").strip()
            password = reg_info.get("password")

            validation_resp = validate.register_validation(user_name, email, password)

            if validation_resp:
                return validation_resp

            email_validation = validate.validate_email(email)
            if email_validation == False:
                return jsonify({"message": "wrong email entered, Please try again"}), 400

            validate_username = validate.validate_characters(user_name)
            if not validate_username:
                return jsonify({"message": "wrong username format entered, Please try again"}), 400

            does_user_exist = is_user_exist(user_name)
            does_email_exist = is_email_exist(email)

            if does_user_exist:
                return jsonify({"message": "Username already exists"}), 409

            elif does_email_exist:
                return jsonify({"message": "Email already exists"}), 409

            else:
                add_new_user(user_name=user_name, email=email, password=password)
                new_user = User(user_name, email, password)
                return jsonify({"New User Created": new_user.__dict__}), 200
        return jsonify({"message": "a 'key(s)' is missing in your registration body"}), 400   
        

class Login(MethodView):
    def post(self):
        login_info = request.get_json()
        search_keys = ("username", "password")

        if all(key in login_info.keys() for key in search_keys):
            user_name = login_info.get("username").strip()
            password = login_info.get("password").strip()

            login_validation = validate.login_validation(user_name, password)
            if login_validation:
                return login_validation

            validate_username = validate.validate_characters(user_name)
            if not validate_username:
                return jsonify({"message": "wrong username format entered, Please try again"}), 400
        

            user_token = {}
            user = get_user_by_username(user_name)

            if user:
                access_token = create_access_token(identity= user["username"])
                user_token["token"] = access_token
                return jsonify(user_token), 200

            return jsonify({"message": "user does not exit, register and login again"}), 404
        return jsonify({"message": "a 'key(s)' is missing in login body"}), 400   

registration_view = RegisterUser.as_view("registration_view")
login_view = Login.as_view("login_view")

auth_blueprint.add_url_rule("/api/auth/register",view_func=registration_view, methods=["POST"])
auth_blueprint.add_url_rule("/api/auth/login",view_func=login_view, methods=["POST"])



