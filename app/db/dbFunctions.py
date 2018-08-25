# Functions to interact with the db

from app.db.dbManager import DBConnection

connect = DBConnection()
cursor = connect.cursor

def add_new_user(userName, email, password):
    #reegister a user
    query = (
        """INSERT INTO users (userName, email, password) VALUES ('{}', '{}', '{}')""".format(userName, email, password))
    cursor.execute(query)

def is_user_exist(userName):
    # check if username exists.
    query = ("""SELECT * FROM users where userName = '{}'""".format(userName))
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


def get_user_by_username(userName):
    #login a user
    query = ("""SELECT * from users where userName = '{}'""".format(userName))
    cursor.execute(query)
    userName = cursor.fetchone()
    return userName

def post_new_question(qstn_tag, question, qstn_owner, date):
    query = (
        """INSERT INTO questions (qstn_tag, question, qstn_owner, date) VALUES ('{}', '{}', '{}', '{}')""".
        format(qstn_tag, question, qstn_owner, date))
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