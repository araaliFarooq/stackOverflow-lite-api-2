import datetime
from flask import jsonify, request, Blueprint, json
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.validation import FieldValidation
from app.models import Question, Answer, Comment
from app.db.dbFunctions import post_new_question, is_question_exist, get_user_by_username, get_all_questions, get_single_question, get_all_answers_to_question, delete_question, get_question_by_id, is_answer_exist, post_new_answer, update_answer, get_answer_details, accept_answer, get_answer_by_id

validate = FieldValidation()
question_blueprint = Blueprint("question_blueprint", __name__)


class PostQuestion(MethodView):
    """class for posting new question"""

    @jwt_required
    def post(self):
        try:
            data = request.get_json()

            search_keys = ("title", "question")

            if all(key in data.keys() for key in search_keys):
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
                    }), 409

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
            return jsonify({"message": "a 'key(s)' is missing in your question body"}), 400   
    
        except:
            return jsonify({"message": "All fields are required"}), 400


class FetchAllQuestions(MethodView):
    """Class to fetch all questions posted"""

    @jwt_required
    def get(self):
        all_questions = get_all_questions()
        if all_questions:
            return jsonify({"All Questions": all_questions}), 200
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
                return jsonify({
                    "Question Details": question_details,
                    "Answers": all_answers
                }), 200
            return jsonify({"message": "Question does not exist"}), 404
        except:
            return jsonify({"message": "Check your url and try again"}), 400


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

        except Exception as exception:
            return jsonify({"message": exception}), 400


class PostAnswerToQuestion(MethodView):
    """class to post an answer to a question"""
    @jwt_required
    def post(self, qstn_id):
        try:
            data = request.get_json()
            search_keys = ("answer")

            if all(key in data.keys() for key in search_keys):
                answer = data.get("answer").strip()

                now = datetime.datetime.now()
                date = now.strftime("%Y-%m-%d %H:%M")
                vote = 0
                status = "pending"

                loggedin_user = get_jwt_identity()
                user = get_user_by_username(user_name=loggedin_user)
                ans_owner = user["username"]

                id_validation = validate.validate_entered_id(qstn_id)
                if id_validation:
                    return id_validation
                    
                ans_validation2 = validate.validate_answer(answer)
                if ans_validation2:
                    return ans_validation2    

                ans_validation = validate.validate_characters(answer)
                if not ans_validation:
                    return jsonify({
                        "message":
                        "wrong answer format entered, Please try again"
                    }), 400

                does_answer_exist = is_answer_exist(qstn_id=qstn_id, answer=answer)
                if does_answer_exist:
                    return jsonify({
                        "message":
                        "Such an answer is already given for this same question, please try with another one"
                    }), 409

                does_qstn_exist = get_question_by_id(qstn_id=qstn_id)
                if not does_qstn_exist:
                    return jsonify({"message": " No such question exists"}), 404

                post_new_answer(
                    answer=answer,
                    ans_owner=ans_owner,
                    qstn_id=qstn_id,
                    vote=vote,
                    status=status,
                    date=date)
                new_answer = Answer(
                    answer=answer,
                    ans_owner=ans_owner,
                    qstn_id=qstn_id,
                    vote=vote,
                    status=status,
                    date=date)
                return jsonify({'New Answer Posted': new_answer.__dict__}), 201

            return jsonify({"message": "a 'key' is missing in your answer body"}), 400   
        except Exception as exception:
            return jsonify({"message": exception}), 400

class UpDateAnswer(MethodView):
    """class to update an answer"""
    @jwt_required
    def put(self,qstn_id, ans_id):
        try:
            qstn_id_validation = validate.validate_entered_id(qstn_id)
            if qstn_id_validation:
                return qstn_id_validation

            ans_id_validation = validate.validate_entered_id(ans_id)
            if ans_id_validation:
                return ans_id_validation

            loggedin_user = get_jwt_identity()
            user = get_user_by_username(user_name=loggedin_user)
            current_user = user["username"]

            does_answer_exist = get_answer_by_id(ans_id=ans_id)
            does_qstn_exist = get_question_by_id(qstn_id=qstn_id)
            ans_owner = get_answer_details(qstn_id, ans_id)
            question_details = get_single_question(qstn_id=qstn_id)
            
            if does_qstn_exist:
                if does_answer_exist:
                    if current_user == ans_owner["ans_owner"]:
                        
                        data = request.get_json()

                        if "answer" in data.keys():
                            answer = data.get("answer").strip()

                            ans_validation2 = validate.validate_answer(answer)
                            if ans_validation2:
                                return ans_validation2    

                            ans_validation = validate.validate_characters(answer)
                            if not ans_validation:
                                return jsonify({
                                    "message":
                                    "wrong answer format entered, Please try again"
                                }), 400

                            update = update_answer(answer=answer,  ans_id=ans_id, qstn_id=qstn_id)
                            return update
                        return jsonify({"message": "Answer 'key' is missing"}), 400  

                    if current_user == question_details["qstn_owner"]:
                        status = "Accepted"

                        accept = accept_answer(status=status, qstn_id=qstn_id, ans_id=ans_id)
                        return accept

                return jsonify({"message": " No such answer exists"}), 404
            return jsonify({"message": " No such question exists any more"}), 404          

        except Exception as exception:
            return jsonify({"message": exception}), 400   


post_question_view = PostQuestion.as_view("post_question_view")
fetch_questions_view = FetchAllQuestions.as_view("fetch_questions_view")
fetch_one_question_view = FetchSingleQuestion.as_view(
    "fetch_one_question_view")
delete_question_view = DeleteQuestion.as_view("delete_question_view")
post_answer_view = PostAnswerToQuestion.as_view("post_answer_view")
update_answer_view = UpDateAnswer.as_view("update_answer_view")

question_blueprint.add_url_rule(
    "/api/questions", view_func=post_question_view, methods=["POST"])
question_blueprint.add_url_rule(
    "/api/questions", view_func=fetch_questions_view, methods=["GET"])
question_blueprint.add_url_rule(
    "/api/questions/<qstn_id>",
    view_func=fetch_one_question_view,
    methods=["GET"])
question_blueprint.add_url_rule(
    "/api/questions/<qstn_id>",
    view_func=delete_question_view,
    methods=["DELETE"])
question_blueprint.add_url_rule(
    "/api/questions/<qstn_id>/answers",
    view_func=post_answer_view,
    methods=["POST"])

question_blueprint.add_url_rule("/api/questions/<qstn_id>/answers/<ans_id>", view_func=update_answer_view, methods=["PUT"])

