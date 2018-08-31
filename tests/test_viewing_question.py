from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json


class Test_Viewing_Question(BaseTestCase):

    
    def test_viewing_all_questions(self):
        """ Test viewing questions """       
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
        response3 = self.app.get("/api/questions",content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']))
        self.assertEquals(response3.status_code, 200)


    def test_viewing_questions_with_db(self):
        """ Test viewing questions """       
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

        response3 = self.app.get("/api/questions",content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']))
        reply = json.loads(response3.data)
        self.assertEquals(reply.get("message"), "No questions posted yet")
        self.assertEquals(response3.status_code, 404)


    def test_viewing_single_question(self):
        """ Test viewing questions """       
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
        response3 = self.app.get("/api/questions/1",content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),data={"qstn_id":"1"})
        self.assertEquals(response3.status_code, 200)
    
    
    def test_deleting_a_questions(self):
        """ Test deleting questions """       
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
        response3 = self.app.delete("/api/questions/1",content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']))

        reply = json.loads(response3.data)
        self.assertEquals(reply.get("message"), "Question successfully deleted")
        self.assertEquals(response3.status_code, 200)


    def test_deleting_a_questions_with_improper_id(self):
        """ Test deleting questions """       
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
        response3 = self.app.delete("/api/questions/q",content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']))

        reply = json.loads(response3.data)
        self.assertEquals(reply.get("message"), "Id should be an interger")
        self.assertEquals(response3.status_code, 400)    
        
    def test_deleting_nonexisting_questions(self):
        """ Test deleting questions """       
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
        response3 = self.app.delete("/api/questions/2",content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']))

        reply = json.loads(response3.data)
        self.assertEquals(reply.get("message"), "Question not deleted, or doesn't exist")
        self.assertEquals(response3.status_code, 400)










BaseTestCase.tearDown            

                        