from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json
from app.models import User


class Test_Posting_Question(BaseTestCase):

    
    def test_adding_offer_with_empty_location(self):
        """ Test for empty location validation """
        
        response1 = self.app.post("/api/auth/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(firstName="Natie", secondName="kyra", userName="araali",
                                                      contact="0888887676", user_category="driver", password="farooq", car_type="rover", reg_num="uab1234", lic_num="4567789999"),)
                                 )
        response = self.app.post(
            "/api/auth/login",
            content_type='application/json',
            data=json.dumps(dict(userName="araali", password="farooq"))
        )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/rides/create_offer",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(location="",
                                                      car_type="Benz", plate_number="uab 123x", contact="08887676", availability="10am - 10pm", cost_per_km="200"),)   
                             ) 

        reply = json.loads(response2.data)
        self.assertEquals(reply.get("message"), "location is missing")
        self.assertEquals(response2.status_code, 400)  

    def test_adding_offer_with_empty_car_type(self):
        """ Test for empty empty car type validation """
        
        response1 = self.app.post("/api/v1/user/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(firstName="Natie", secondName="kyra", userName="araali",
                                                      contact="0888887676", user_category="driver", password="farooq", car_type="rover", reg_num="uab1234", lic_num="4567789999"),)
                                 )
        response = self.app.post(
            "/api/v1/user/login",
            content_type='application/json',
            data=json.dumps(dict(userName="araali", password="farooq"))
        )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/rides/create_offer",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(location="kawempe",
                                                      car_type="", plate_number="uab 123x", contact="08887676", availability="10am - 10pm", cost_per_km="200"),)   
                             ) 

        reply = json.loads(response2.data)
        self.assertEquals(reply.get("message"), "car type is missing")
        self.assertEquals(response2.status_code, 400)  

    def test_adding_offer_with_empty_plate_number(self):
        """ Test for empty number plate validation """
        
        response1 = self.app.post("/api/v1/user/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(firstName="Natie", secondName="kyra", userName="araali",
                                                      contact="0888887676", user_category="driver", password="farooq", car_type="rover", reg_num="uab1234", lic_num="4567789999"),)
                                 )
        response = self.app.post(
            "/api/v1/user/login",
            content_type='application/json',
            data=json.dumps(dict(userName="araali", password="farooq"))
        )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/rides/create_offer",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(location="kawempe",
                                                      car_type="Benz", plate_number="", contact="08887676", availability="10am - 10pm", cost_per_km="200"),)   
                             ) 

        reply = json.loads(response2.data)
        self.assertEquals(reply.get("message"), "plate number is missing")
        self.assertEquals(response2.status_code, 400)  


    def test_adding_offer_with_empty_contact(self):
        """ Test for empty contact validation """
        
        response1 = self.app.post("/api/v1/user/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(firstName="Natie", secondName="kyra", userName="araali",
                                                      contact="0888887676", user_category="driver", password="farooq", car_type="rover", reg_num="uab1234", lic_num="4567789999"),)
                                 )
        response = self.app.post(
            "/api/v1/user/login",
            content_type='application/json',
            data=json.dumps(dict(userName="araali", password="farooq"))
        )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/rides/create_offer",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(location="kawempe",
                                                      car_type="Benz", plate_number="uab 123x", contact="", availability="10am - 10pm", cost_per_km="200"),)   
                             ) 

        reply = json.loads(response2.data)
        self.assertEquals(reply.get("message"), "contact is missing")
        self.assertEquals(response2.status_code, 400)  


    def test_adding_offer_with_empty_availability(self):
        """ Test for empty availability validation """
        
        response1 = self.app.post("/api/v1/user/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(firstName="Natie", secondName="kyra", userName="araali",
                                                      contact="0888887676", user_category="driver", password="farooq", car_type="rover", reg_num="uab1234", lic_num="4567789999"),)
                                 )
        response = self.app.post(
            "/api/v1/user/login",
            content_type='application/json',
            data=json.dumps(dict(userName="araali", password="farooq"))
        )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/rides/create_offer",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(location="kawempe",
                                                      car_type="Benz", plate_number="uab 123x", contact="08887676", availability="", cost_per_km="200"),)   
                             ) 

        reply = json.loads(response2.data)
        self.assertEquals(reply.get("message"), "working hours not stated")
        self.assertEquals(response2.status_code, 400)  


    def test_adding_offer_with_empty_cost_per_km(self):
        """ Test for empty cost per km validation """
        
        response1 = self.app.post("/api/v1/user/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(firstName="Natie", secondName="kyra", userName="araali",
                                                      contact="0888887676", user_category="driver", password="farooq", car_type="rover", reg_num="uab1234", lic_num="4567789999"),)
                                 )
        response = self.app.post(
            "/api/v1/user/login",
            content_type='application/json',
            data=json.dumps(dict(userName="araali", password="farooq"))
        )
        reply2 = json.loads(response.data.decode())

        response2 = self.app.post("/api/v1/rides/create_offer",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+reply2['token']),
                                 data=json.dumps(dict(location="kawempe",
                                                      car_type="Benz", plate_number="uab 123x", contact="08887676", availability="10am - 10pm", cost_per_km=""),)   
                             ) 

        reply = json.loads(response2.data)
        self.assertEquals(reply.get("message"), "charge per Km not stated")
        self.assertEquals(response2.status_code, 400)
    
    