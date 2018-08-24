# Model class.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Question:
    def __init__(self, qstn_tag, question, qstn_owner, date):
        self.qstn_tag = qstn_tag
        self.question = question
        self.qstn_owner = qstn_owner
        self.date = date

class Answer:
    def __init__(self, answer, ans_owner, qstn_id, date):
        self.answer = answer
        self.ans_owner = ans_owner
        self.qstn_id = qstn_id
        self.date = date

class Comment:
    def __init__(self, comment, comment_owner, ans_id, date):
        self.comment = comment
        self.comment_owner = comment_owner
        self.ans_id = ans_id
        self.date = date