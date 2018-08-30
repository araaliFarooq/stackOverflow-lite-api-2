from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json
from app.models import User


class Test_Posting_Question(BaseTestCase):

    
    def test_posting_new_question(self):
        """ Test posting question """
        
        response1 = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali2", email="22araali@email.com", password="araali"),)
                                 )
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="araali2", password="araali"))
        )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/questions",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(title="Life", question="Are there so many questions about life?"),)   
                             ) 
        self.assertEquals(response2.status_code, 201)


    def test_posting_existing_question(self):
        """ Test posting a question """
        
        response1 = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali2", email="22araali@email.com", password="araali"),)
                                 )
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="araali2", password="araali"))
        )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/questions",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(title="Life", question="Are there so many questions about life?"),)   
                             )
        response2 = self.app.post("/api/questions",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(title="Life style", question="Are there so many questions about life?"),)   
                             )                       

        reply = json.loads(response2.data)
        self.assertEquals(reply.get("message"), "Question already exists, check it out for an answer")
        self.assertEquals(response2.status_code, 409)


    def test_posting_with_empty_question(self):
        """ Test posting a question """
        
        response1 = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali2", email="22araali@email.com", password="araali"),)
                                 )
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="araali2", password="araali"))
        )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/questions",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(title="Life", question=" "),)   
                             )
       
        reply = json.loads(response2.data)
        self.assertEquals(reply.get("message"), "No question was given")
        self.assertEquals(response2.status_code, 400)  


    def test_posting_with_empty_title(self):
        """ Test posting a question """
        
        response1 = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali2", email="22araali@email.com", password="araali"),)
                                 )
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="araali2", password="araali"))
        )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/questions",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(title="", question=" Are there so many questions about life"),)   
                             )
       
        reply = json.loads(response2.data)
        self.assertEquals(reply.get("message"), "No question title was given")
        self.assertEquals(response2.status_code, 400)                   
          

BaseTestCase.tearDown
    
    