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
    # check if user exists.
    query = ("""SELECT COUNT(*) FROM users where userName = '{}'""".format(userName))
    cursor.execute(query)
    user = cursor.fetchone()
    if user > 0:
        return True
    return False    


def get_user_by_username(userName):
    #login a user
    query = ("""SELECT * from users where userName = '{}'""".format(userName))
    cursor.execute(query)
    userName = cursor.fetchone()
    return userName