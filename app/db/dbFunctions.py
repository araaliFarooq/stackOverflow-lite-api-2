# Functions to interact with the db

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
    query = ("""DELETE FROM questions WHERE qstn_id = '{}' and qstn_owner = '{}'""" .format(qstn_id, user_name))
    delete = cursor.execute(query)
    return delete