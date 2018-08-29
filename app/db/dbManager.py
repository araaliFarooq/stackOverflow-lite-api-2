import psycopg2
import psycopg2.extras as extra
from pprint import pprint
from app import app
from app.config import app_config


class DBConnection:
    def __init__(self):
        if app_config["testing"]:
            self.con = psycopg2.connect(database="stackoverflow_tests", user="postgres", password="araali", host="localhost",port="5432")
            self.con.autocommit = True
            self.cursor = self.con.cursor()
            self.dict_cursor = self.con.cursor(cursor_factory=extra.RealDictCursor)
        elif app_config["development"]:
            self.con = psycopg2.connect(database="stackoverflow", user="postgres", password="araali", host="localhost",port="5432")
            self.con.autocommit = True
            self.cursor = self.con.cursor()
            self.dict_cursor = self.con.cursor(cursor_factory=extra.RealDictCursor)      

    def create_tables(self):
		
        queries = (
			"""
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL,
                password VARCHAR(25) NOT NULL
            )
            """,

			"""
			CREATE TABLE IF NOT EXISTS questions (
				qstn_id SERIAL PRIMARY KEY,
					title VARCHAR(20) NOT NULL,
					question VARCHAR(250) NOT NULL,
					qstn_owner VARCHAR(20) NOT NULL,
                    date timestamp NOT NULL
							
						)
						""",

			"""
            CREATE TABLE IF NOT EXISTS answers (
                ans_id SERIAL PRIMARY KEY,
                answer VARCHAR(250) NOT NULL,
                ans_owner VARCHAR(20) NOT NULL,
                qstn_id INTEGER NOT NULL,
                votes INTEGER NOT NULL,
                status VARCHAR(250) NOT NULL,
                date timestamp NOT NULL
            )
            """,
			"""
            CREATE TABLE IF NOT EXISTS comments (
                comment_id SERIAL PRIMARY KEY,
                comment VARCHAR(250) NOT NULL,
                comment_owner VARCHAR(20) NOT NULL,
                ans_id INTEGER NOT NULL,
                date timestamp NOT NULL
            )
            """
        )
        for query in queries:
            self.cursor.execute(query)

    def create_test_tables(self):
		
        queries = (
			"""
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL,
                password VARCHAR(25) NOT NULL
            )
            """,

			"""
			CREATE TABLE IF NOT EXISTS questions (
				qstn_id SERIAL PRIMARY KEY,
					title VARCHAR(20) NOT NULL,
					question VARCHAR(250) NOT NULL,
					qstn_owner VARCHAR(20) NOT NULL,
                    date timestamp NOT NULL
							
						)
						""",

			"""
            CREATE TABLE IF NOT EXISTS answers (
                ans_id SERIAL PRIMARY KEY,
                answer VARCHAR(250) NOT NULL,
                ans_owner VARCHAR(20) NOT NULL,
                qstn_id INTEGER NOT NULL,
                votes INTEGER NOT NULL,
                status VARCHAR(250) NOT NULL,
                date timestamp NOT NULL
            )
            """,
			"""
            CREATE TABLE IF NOT EXISTS comments (
                comment_id SERIAL PRIMARY KEY,
                comment VARCHAR(250) NOT NULL,
                comment_owner VARCHAR(20) NOT NULL,
                ans_id INTEGER NOT NULL,
                date timestamp NOT NULL
            )
            """
        )
        for query in queries:
            self.cursor.execute(query)


    def delete_test_tables(self):

        delete_queries = (
            """
            DROP TABLE IF EXISTS users CASCADE
            """,

            """
			DROP TABLE IF EXISTS questions CASCADE
						""",

            """
            DROP TABLE IF EXISTS answers CASCADE
            """,
            """
            DROP TABLE IF EXISTS comments CASCADE
            """
        )
        for query in delete_queries:
            self.cursor.execute(query)        