from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class Test_auth(BaseTestCase):

    def test_registration(self):
        """ Test for successful user register """
        response = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali2", email="22araali@email.com", password="araali"),)
                                 )
        self.assertEquals(response.status_code, 201)

    def test_registration_with_empty_user_name(self):
        """ Test for empty username validation """

        response = self.app.post(
            "/api/auth/register",
            content_type='application/json',
            data=json.dumps(dict(username=" ", email="22araali@email.com", password="araali"),)
        )
        reply = json.loads(response.data)
        self.assertEquals(reply.get("message"), "username is missing")
        self.assertEquals(response.status_code, 400)

    def test_registration_with_empty_password(self):
        """ Test for empty password validation """
        response = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali", email="22araali@email.com", password=""),)
                                 )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "password is missing")
        self.assertEquals(response.status_code, 400)

    def test_registration_with_empty_email(self):
        """ Test for empty email validation """
        response = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali", email=" ", password="araali"),)
                                 )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "email is missing")
        self.assertEquals(response.status_code, 400)

    def test_registration_with_wrong_username_format(self):
        """ Test for empty contact validation """

        response = self.app.post(
            "/api/auth/register",
            content_type='application/json',
            data=json.dumps(dict(username="@@@@@@", email="araali@email.com", password="araali"),)
        )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "wrong username format entered, Please try again")
        self.assertEquals(response.status_code, 400)

    def test_registration_with_wrong_email_format(self):
        """ Test for empty contact validation """

        response = self.app.post(
            "/api/auth/register",
            content_type='application/json',
            data=json.dumps(dict(username="araali", email="araalfarooq", password="araali"),)
        )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "wrong email entered, Please try again")
        self.assertEquals(response.status_code, 400)

    def test_user_exists(self):
        """ Test for username exist """
        response = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali2", email="22araali@email.com", password="araali"),)
                                 )
        response = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali2", email="22araali@email.com", password="araali"),)
                                 )

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Username already exists")
        self.assertEquals(response.status_code, 409)

    def test_email_exists(self):
        """ Test for username exist """
        response = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali", email="22araali@email.com", password="araali"),)
                                 )
        response = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali2", email="22araali@email.com", password="araali"),)
                                 )

        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Email already exists")
        self.assertEquals(response.status_code, 409)    

    def test_registration_with_no_keys(self):
        """ test_registration_with-no_keys """

        response = self.app.post(
            "/api/auth/register",
            content_type='application/json',
            data=json.dumps(dict( email="22araali@email.com", password="araali"),)
        )
        reply = json.loads(response.data)
        self.assertEquals(reply.get("message"), "a 'key(s)' is missing in your registration body")
        self.assertEquals(response.status_code, 400)

   
   
    def test_user_login_successful(self):
        """ Test for successful login """
        response2 = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="araali", email="22araali@email.com", password="araali"),)
                                 )

        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="araali", password="araali"))
        )
        reply = json.loads(response.data)

        self.assertEquals(response.status_code, 200)

    def test_user_login_with_wrong_or_no_password(self):
        """ Test for login with wrong or no password """

        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="araali", password=""))
        )
        reply = json.loads(response.data)

        self.assertEquals(reply["message"], "password is missing")
        self.assertEquals(response.status_code, 400)

    def test_user_login_with_wrong_or_no_username(self):
        """ Test for login with wrong or no username """

        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="", password="farooq"))
        )
        reply = json.loads(response.data)

        self.assertEquals(reply["message"], "username is missing")
        self.assertEquals(response.status_code, 400)

    def test_user_login_with_wrong_or_improper_username(self):
        """ Test for login with wrong or no username """

        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(username="@@@@@", password="farooq"))
        )
        reply = json.loads(response.data)

        self.assertEquals(reply["message"], "wrong username format entered, Please try again")
        self.assertEquals(response.status_code, 400)

    def test_user_login_with_missing_keys(self):
        """ Test for login with wrong or no username """

        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict( password="farooq"))
        )
        reply = json.loads(response.data)

        self.assertEquals(reply["message"], "a 'key(s)' is missing in login body")
        self.assertEquals(response.status_code, 400)        

BaseTestCase.tearDown
