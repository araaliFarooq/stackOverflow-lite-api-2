import datetime
from flask import jsonify, request, Blueprint
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.validation import FieldValidation
from app.models import Question, Answer, Comment
from app.db.dbFunctions import post_new_question, is_question_exist, get_user_by_username

validate = FieldValidation()
question_blueprint = Blueprint("question_blueprint", __name__)

class PostQuestion(MethodView):
    """class for posting new question"""
    def post(self):
        data = request.get_json()
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M")

        loggedin_user = get_jwt_identity()
        user = get_user_by_username(username=loggedin_user)

        qstn_owner = user[1]
        qstn_tag = data.gte("qstn_tag").strip()
        question = data.get("question").strip()

        validation = validate.validate_question(qstn_tag, question)
        if validation:
            return validation

        does_qstn_exist = is_question_exist(question)
        if does_qstn_exist:
            return jsonify({"message": "Question already exists, check it out for an answer"}), 400

        post_new_question(qstn_tag=qstn_tag, question=question, qstn_owner=qstn_owner, date=date)
        new_question = Question(qstn_tag=qstn_tag, question=question, qstn_owner=qstn_owner, date=date)
        return jsonify({'New Question Posted': new_question.__dict__}), 201

        

