import datetime
from flask import jsonify, request, Blueprint, json
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.validation import FieldValidation
from app.models import Question, Answer, Comment
from app.db.dbFunctions import post_new_question, is_question_exist, get_user_by_username, get_all_questions, get_single_question,get_all_answers_to_question, delete_question

validate = FieldValidation()
question_blueprint = Blueprint("question_blueprint", __name__)


class PostQuestion(MethodView):
    """class for posting new question"""
    @jwt_required
    def post(self):
        try:
            data = request.get_json()
            now = datetime.datetime.now()
            date = now.strftime("%Y-%m-%d %H:%M")

            loggedin_user = get_jwt_identity()
            user = get_user_by_username(user_name=loggedin_user)

            qstn_owner = user["username"]
            title = data.get("title").strip()
            question = data.get("question").strip()

            validation = validate.validate_question(title, question)
            if validation:
                return validation

            does_qstn_exist = is_question_exist(question)
            if does_qstn_exist:
                return jsonify({
                    "message":
                    "Question already exists, check it out for an answer"
                }), 400

            post_new_question(
                title=title,
                question=question,
                qstn_owner=qstn_owner,
                date=date)
            new_question = Question(
                title=title,
                question=question,
                qstn_owner=qstn_owner,
                date=date)
            return jsonify({'New Question Posted': new_question.__dict__}), 201
        except:
            return jsonify({"message":"All fields are required"}),400


class FetchAllQuestions(MethodView):
    """Class to fetch all questions posted"""
    @jwt_required
    def get(self):
        all_questions = get_all_questions()
        if all_questions:
            return jsonify({"All Questions":all_questions}), 200
        return jsonify({"message": "No questions posted yet"}), 404


class FetchSingleQuestion(MethodView):
    """class to get single question"""
    @jwt_required
    def get(self, qstn_id):
        try:
            id_validation = validate.validate_entered_id(qstn_id)
            if id_validation:
                return id_validation

            question_details = get_single_question(qstn_id=qstn_id)
            all_answers = get_all_answers_to_question(qstn_id=qstn_id)
            if question_details:
                return jsonify({"Question Details": question_details,
                "Answers":all_answers
                }), 200
            return jsonify({"message": "Question does not exit"}), 404
        except:
            return jsonify({"message":"Check your url and try again"}), 400

class DeleteQuestion(MethodView):
    """Delete a specific question"""
    @jwt_required
    def delete(self, qstn_id):
        try:
            id_validation = validate.validate_entered_id(qstn_id)
            if id_validation:
                return id_validation

            loggedin_user = get_jwt_identity()
            user = get_user_by_username(user_name=loggedin_user)
            qstn_owner = user["username"]
            delete = delete_question(qstn_id=qstn_id, user_name=qstn_owner)
            return delete

        except:
            return jsonify({"message":"Check your url and try again"}),400




post_question_view = PostQuestion.as_view("post_question_view")
fetch_questions_view = FetchAllQuestions.as_view("fetch_questions_view")
fetch_one_question_view = FetchSingleQuestion.as_view(
    "fetch_one_question_view")
delete_question_view = DeleteQuestion.as_view("delete_question_view")    

question_blueprint.add_url_rule(
    "/api/questions", view_func=post_question_view, methods=["POST"])
question_blueprint.add_url_rule(
    "/api/questions", view_func=fetch_questions_view, methods=["GET"])
question_blueprint.add_url_rule(
    "/api/questions/<qstn_id>",
    view_func=fetch_one_question_view,
    methods=["GET"])
question_blueprint.add_url_rule("/api/questions/<qstn_id>", view_func=delete_question_view, methods=["DELETE"])