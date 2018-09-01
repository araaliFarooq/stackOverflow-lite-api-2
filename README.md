# stackOverflow-lite-api-2

[![Build Status](https://travis-ci.org/araaliFarooq/stackOverflow-lite-api-2.svg?branch=challenge_3)](https://travis-ci.org/araaliFarooq/stackOverflow-lite-api-2)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8be53303a1be4577a6f1a2ea1aa62f6b)](https://www.codacy.com/app/araaliFarooq/stackOverflow-lite-api-2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=araaliFarooq/stackOverflow-lite-api-2&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/araaliFarooq/stackOverflow-lite-api-2/badge.svg?branch=challenge_3)](https://coveralls.io/github/araaliFarooq/stackOverflow-lite-api-2?branch=challenge_3)


## About
This is an API for a Question and Answer (Q&A) application that allows users to ask questions to which other users can give answers.

##Demo Link:
- https://araalifarooq.docs.apiary.io/#

## Features
- Register a user
- Login a user
- Get all the questions posted on the app
- Post any question on the app.
- Post an answer to a given question.
- Accept or reject an answer given to your question.
- View all answers to a specific question.
- Update your answer to a given question

## Other features
- View all questions you have ever posted

## Tools Used
- [Flask](http://flask.pocoo.org/) - web microframework for Python
- [PostgreSQL](https://www.postgresql.org/)- Open source relational database

## Requirements
Python 3.6
 
## Run (Use) on your local machine
First clone the repository
```sh
   $ git clone https://github.com/araaliFarooq/stackOverflow-lite-api-2
   ```
   Head over to the cloned directory, create a virtual environment, use pip to install the requirements, then run the app
   ```sh
    $ cd stackOverflow-lite-api-2
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python run.py
```
#### Endpoints to create a user account and login into the application
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/auth/register | True | Create a user account
POST | /api/auth/login | True | Login a user

#### Endpoints to create, read, update, and delete questions and answers
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/questions | False | Post a Question
GET | /api/questions | False | Fetch all Questions
GET | /api/questions/<qstn_id> | False | Fetch a single question
POST | /api/questions/<qstn_id>/answers | False | Post an answer to a question
DELETE | /api/questions/<qstn_id> | False | Delete a question
PUT | /api/questions/<qstn_id>/answers/<ans_id>| False | Accept an answer or Update an answer
GET | /api/questions/all_questions | False | Fetch all Questions you have ever posted



