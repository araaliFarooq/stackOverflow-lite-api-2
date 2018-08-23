# Model class.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Question:
    def __init__(self, qstn_id, qstn_tag, question, qstn_owner):
        self.qstn_id = qstn_id
        self.qstn_tag = qstn_tag
        self.question = question
        self.qstn_owner = qstn_owner

class Answer:
    def __init__(self, ans_id, answer, ans_owner, qstn_id):
        self.ans_id = ans_id
        self.answer = answer
        self.ans_owner = ans_owner
        self.qstn_id = qstn_id

class Comments:
    def __init__(self, comment, comment_owner, ans_id):
        self.comment = comment
        self.comment_owner = comment_owner
        self.ans_id = ans_id