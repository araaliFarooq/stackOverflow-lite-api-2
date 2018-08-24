from flask import jsonify
import re

class FieldValidation:

    def client_validation(self, userName, password):
        if not userName:
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

    
    def validate_question(self, qstn_tag, question):
        if not qstn_tag:
            return jsonify({"message": "No question tag was given"}), 400
        if not question:
            return jsonify({"message": "No question was given"}), 400
        if len(question) < 10:
            return jsonify({"message": "Question has to be at least 10 characters long"}), 400

    
    def validate_email(self, email):
        if len(email) > 7:
            if re.match("[^@]+@[^@]+\.[^@]+", email) != None:
                return True
            return False
        return False 
