from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json


class Test_Posting_Answer(BaseTestCase):

    
    def test_posting_answer(self):
        """ Test posting answer """       
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
        response3 = self.app.post("/api/questions/1/answers",
                                content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                data=json.dumps(dict(answer="Are there so many questions about life?"),)   
                            )
        self.assertEquals(response3.status_code, 201)

    
    def test_updating_answer_as_answer_owner(self):
        """ Test posting answer """       
        response1 = self.app.post("/api/auth/register",
                                    content_type='application/json',
                                    data=json.dumps(dict(username="araali2", email="araali@email.com", password="araali"),)
                                    )

        response1 = self.app.post("/api/auth/register",
                                    content_type='application/json',
                                    data=json.dumps(dict(username="araali3", email="2araali@email.com", password="araali"),)
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
        _response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="araali3", password="araali"))
        )
        reply3 = json.loads(_response.data.decode())

        response3 = self.app.post("/api/questions/1/answers",
                                content_type='application/json', headers=dict(Authorization='Bearer '+reply3['token']),
                                data=json.dumps(dict(answer="Are there so many questions about life?"),)   
                            )
        response4 = self.app.put("/api/questions/1/answers/1",
                                content_type='application/json', headers=dict(Authorization='Bearer '+reply3['token']),
                                data=json.dumps(dict(answer="Are there so many questions about life unanswered?"),)   
                            )                    
        reply4 = json.loads(response4.data)
        self.assertEquals(reply4.get("message"), "Answer successfully updated")
        self.assertEquals(response4.status_code, 200)


    def test_updating_answer_as_question_owner(self):
        """ Test posting answer """       
        response1 = self.app.post("/api/auth/register",
                                    content_type='application/json',
                                    data=json.dumps(dict(username="araali2", email="araali@email.com", password="araali"),)
                                    )

        response1 = self.app.post("/api/auth/register",
                                    content_type='application/json',
                                    data=json.dumps(dict(username="araali3", email="2araali@email.com", password="araali"),)
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
        _response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="araali3", password="araali"))
        )
        reply3 = json.loads(_response.data.decode())

        response3 = self.app.post("/api/questions/1/answers",
                                content_type='application/json', headers=dict(Authorization='Bearer '+reply3['token']),
                                data=json.dumps(dict(answer="Are there so many questions about life?"),)   
                            )
        response4 = self.app.put("/api/questions/1/answers/1",
                                content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                data=json.dumps(dict(answer="Are there so many questions about life unanswered?"),)   
                            )                    
        reply4 = json.loads(response4.data)
        self.assertEquals(reply4.get("message"), "Answer successfully accepted")
        self.assertEquals(response4.status_code, 200)   

    def test_updating_nonexistant_answer_as_answer_owner(self):
        """ Test posting answer """       
        response1 = self.app.post("/api/auth/register",
                                    content_type='application/json',
                                    data=json.dumps(dict(username="araali2", email="araali@email.com", password="araali"),)
                                    )

        response1 = self.app.post("/api/auth/register",
                                    content_type='application/json',
                                    data=json.dumps(dict(username="araali3", email="2araali@email.com", password="araali"),)
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
        _response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="araali3", password="araali"))
        )
        reply3 = json.loads(_response.data.decode())

        response3 = self.app.post("/api/questions/1/answers",
                                content_type='application/json', headers=dict(Authorization='Bearer '+reply3['token']),
                                data=json.dumps(dict(answer="Are there so many questions about life?"),)   
                            )
        response4 = self.app.put("/api/questions/1/answers/2",
                                content_type='application/json', headers=dict(Authorization='Bearer '+reply3['token']),
                                data=json.dumps(dict(answer="Are there so many questions about life unanswered?"),)   
                            )                    
        reply4 = json.loads(response4.data)
        self.assertEquals(reply4.get("message"), "No such answer exists")
        self.assertEquals(response4.status_code, 404) 

    def test_updating_nonexistant_answer_as_question_owner(self):
        """ Test posting answer """       
        response1 = self.app.post("/api/auth/register",
                                    content_type='application/json',
                                    data=json.dumps(dict(username="araali2", email="araali@email.com", password="araali"),)
                                    )

        response1 = self.app.post("/api/auth/register",
                                    content_type='application/json',
                                    data=json.dumps(dict(username="araali3", email="2araali@email.com", password="araali"),)
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
        _response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="araali3", password="araali"))
        )
        reply3 = json.loads(_response.data.decode())

        response3 = self.app.post("/api/questions/1/answers",
                                content_type='application/json', headers=dict(Authorization='Bearer '+reply3['token']),
                                data=json.dumps(dict(answer="Are there so many questions about life?"),)   
                            )
        response4 = self.app.put("/api/questions/2/answers/1",
                                content_type='application/json', headers=dict(Authorization='Bearer '+reply3['token']),
                                data=json.dumps(dict(answer="Are there so many questions about life unanswered?"),)   
                            )                    
        reply4 = json.loads(response4.data)
        self.assertEquals(reply4.get("message"), "No such question exists any more")
        self.assertEquals(response4.status_code, 404) 






BaseTestCase.tearDown
