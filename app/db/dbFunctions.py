# Functions to interact with the db

from flask import jsonify
from app.db.dbManager import DBConnection

connect = DBConnection()
cursor = connect.dict_cursor

def add_new_user(user_name, email, password):
    #reegister a user
    query = (
        """INSERT INTO users (username, email, password) VALUES ('{}', '{}', '{}')""".format(user_name, email, password))
    cursor.execute(query)

def is_user_exist(user_name):
    # check if username exists.
    query = ("""SELECT * FROM users where username = '{}'""".format(user_name))
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return True
    return False    

def is_email_exist(email):
    # check if user email exists.
    query = ("""SELECT * FROM users where email = '{}'""".format(email))
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return True
    return False        


def get_user_by_username(user_name):
    #login a user
    query = ("""SELECT * from users where username = '{}'""".format(user_name))
    cursor.execute(query)
    user_name = cursor.fetchone()
    return user_name

def post_new_question(title, question, qstn_owner, date):
    query = (
        """INSERT INTO questions (title, question, qstn_owner, date) VALUES ('{}', '{}', '{}', '{}')""".
        format(title, question, qstn_owner, date))
    cursor.execute(query)

def is_question_exist(question):
    # check if question exists.
    query = ("""SELECT * FROM questions where question = '{}'""".format(question))
    cursor.execute(query)
    question = cursor.fetchone()
    if question:
        return True
    return False

def get_all_questions():
    #function to get all posted questions
    cursor.execute("SELECT * from questions")
    all_questions = cursor.fetchall()
    return all_questions  

def get_single_question(qstn_id):
    """ function to get details of a question"""
    cursor.execute("SELECT * FROM questions WHERE qstn_id = '{}'" .format(qstn_id))
    row = cursor.fetchone()
    return row

def get_all_answers_to_question(qstn_id):
    #get_all_answers_to_question
    query = ("""SELECT * from answers where qstn_id = '{}'""".format(qstn_id))
    cursor.execute(query)
    answers = cursor.fetchall()
    return answers

def delete_question(qstn_id, user_name):
    """function to delete a specific question"""
    try:
        query = ("""DELETE FROM questions WHERE qstn_id = '{}' and qstn_owner = '{}'""" .format(qstn_id, user_name))
        cursor.execute(query)
        delete = cursor.rowcount

        if int(delete) > 0:
            return jsonify({"message":"Question successfully deleted"}),200
        else:
            return jsonify({"message":"Question not deleted, or doesn't exist"}),400   

    except Exception as exception:
        return jsonify({"message":str(exception)}),400

def is_answer_exist(qstn_id, answer):
    # check if answer exists.
    query = ("""SELECT * FROM answers WHERE qstn_id = '{}' and answer = '{}'""" .format(qstn_id, answer))
    cursor.execute(query)
    answer = cursor.fetchone()
    if answer:
        return True
    return False   

def get_question_by_id(qstn_id):
    # check if question exists.
    query = ("""SELECT * FROM questions where qstn_id = '{}'""".format(qstn_id))
    cursor.execute(query)
    question = cursor.fetchone()
    if question:
        return True
    return False

def get_answer_by_id(ans_id):
    # check if answer exists.
    query = ("""SELECT * FROM answers where ans_id = '{}'""".format(ans_id))
    cursor.execute(query)
    answer = cursor.fetchone()
    if answer:
        return True
    return False    

def post_new_answer(answer, ans_owner, qstn_id, vote, status, date):
    #post a new answer
    query = (
        """INSERT INTO answers (answer, ans_owner, qstn_id, votes, status, date) VALUES ('{}', '{}', '{}','{}', '{}', '{}')""".format(answer, ans_owner, qstn_id, vote, status, date))
    cursor.execute(query)


def update_answer(answer, ans_id, qstn_id):
    """function to update answer"""
    try:
        query = ("""UPDATE answers SET answer = '{}' where ans_id = '{}' and qstn_id = '{}'""" .format(
            answer, ans_id, qstn_id))
        cursor.execute(query)
        count = cursor.rowcount
        if int(count) > 0:
            return "Answer successfully updated"
        else:
            return "Answer not updated, or doesn't exist"   

    except Exception as exception:
        return jsonify({"message":str(exception)}),400   

def accept_answer(status, qstn_id, ans_id):
    """function to accept or reject answer"""
    try:
        query = ("""UPDATE answers SET status = '{}' where ans_id = '{}' and qstn_id = '{}'""" .format(
            status, ans_id, qstn_id))
        cursor.execute(query)
        count = cursor.rowcount
        if int(count) > 0:
            return "Answer successfully accepted"
        else:
            return "Failed to accept answer, or it doesn't exist"

    except Exception as exception:
        return jsonify({"message":str(exception)}),400   


def get_answer_details(qstn_id, ans_id):
    """ function to get details of a question"""
    cursor.execute("""SELECT * FROM answers WHERE qstn_id = '{}' and ans_id = '{}'""".format(qstn_id, ans_id))
    row = cursor.fetchone()
    return row




        

    