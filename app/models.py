# Model class.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Question:
    def __init__(self, title, question, qstn_owner, date):
        self.title = title
        self.question = question
        self.qstn_owner = qstn_owner
        self.date = date

    def toJson(self):
        """Function to give the question model ability to be jsonified """
        question = dict(
            title=self.title,
            question=self.question,
            qstn_owner=self.qstn_owner,
            date=self.date
        )
        return question   

    # method to enable us display class objects as dictionaries 
    def __repr__(self):
        return repr(self.__dict__)

class Answer:
    def __init__(self, answer, ans_owner, qstn_id, vote, status, date):
        self.answer = answer
        self.ans_owner = ans_owner
        self.qstn_id = qstn_id
        self.vote = vote
        self.status = status
        self.date = date

class Comment:
    def __init__(self, comment, comment_owner, ans_id, date):
        self.comment = comment
        self.comment_owner = comment_owner
        self.ans_id = ans_id
        self.date = date