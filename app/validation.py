from flask import jsonify
import re

class FieldValidation:

    def register_validation(self, user_name, email, password):
        if not user_name:
            return jsonify({"message": "username is missing"}), 400
        if not email:
            return jsonify({"message": "email is missing"}), 400
        if not password:
            return jsonify({"message": "password is missing"}), 400
        if len(password) < 5:
            return jsonify({"message": "password should be at least 5 characters long"}), 400    


    def login_validation(self, user_name, password):
        if not user_name:
            return jsonify({"message": "username is missing"}), 400
        if not password:
            return jsonify({"message": "password is missing"}), 400
        if len(password) < 5:
            return jsonify({"message": "password should be at least 5 characters long"}), 400            

   
    def validate_entered_id(self,id):
        try:
           _id = int(id)
        except ValueError:
            return jsonify({"message": "Id should be an interger"}), 400

    
    def validate_question(self, title, question):
        if not title:
            return jsonify({"message": "No question tag was given"}), 400
        if not question:
            return jsonify({"message": "No question was given"}), 400
        if len(title) < 4:
            return jsonify({"message": "Title has to be at least 4 characters long"}), 400
        if len(question) < 10:
            return jsonify({"message": "Question has to be at least 10 characters long"}), 400

    
    def validate_email(self, email):
        if len(email) > 7:
            if re.match("[^@]+@[^@]+\.[^@]+", email) != None:
                return True
            return False
        return False

    def validate_type(self, input):
        if re.match("^[1-9]\d*(\.\d+)?$", input) != None:
            return True
        return False

    def validate_characters(self, input):
        if re.search('[a-zA-Z]', input) != None:
            return True
        return False    

    def validate_answer(self, answer):
        if not answer:
            return jsonify({"message": "No answer was given"}), 400
        if len(answer) < 10:
            return jsonify({"message": "Answer has to be at least 10 characters long"}), 400

    
