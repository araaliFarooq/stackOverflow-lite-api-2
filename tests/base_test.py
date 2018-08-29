import unittest
from run import app
from app.config import app_config
from app.db.dbManager import DBConnection

connection = DBConnection()

class BaseTestCase(unittest.TestCase):

    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.app = app.test_client(self)
        connection.create_test_tables()
        
    def tearDown(self):
        """
        Method to droP tables after the test is run
        """
        connection.delete_test_tables()
       