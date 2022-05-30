- [About the project](#about-the-project)
- [How to start a project](#how-to-start-a-project)
- [API request and response examples](#api-request-and-response-examples)

#### About the project

Django REST framework training project. Built on viewsets with different access levels allowing you to make changes to the database.

JWT tokens are used for authentication.

Unauthorized users have read-only access to the API. Authorized users are allowed to change their content, otherwise, access is read-only.

#### How to start a project

- 	Clone the repository and change into it on the command line:

        git clone https://github.com/Gollum959/api_final_yatube.git
        cd api_final_yatube
- Create and activate virtual environment:

        python3 -m venv env
        source env/bin/activate
- Install dependencies from a file requirements.txt

        python3 -m pip install --upgrade pip
        pip install -r requirements.txt
- Run migrations:

        python3 manage.py migrate
- Run project:

        python3 manage.py runserver

#### API request and response examples

**- Get JWT token**

POST http://127.0.0.1:8000/api/v1/jwt/create/

**Request samples**

    application/json
    {
    	"username": "string",
    	"password": "string"
    }
**Response samples**

    {
    	"refresh": "string",
    	"access": "string"
    }

**- Get a list of all publications**

GET http://127.0.0.1:8000/api/v1/posts/

**Response samples**

    application/json
    {
    	"count": 123,
    	"next": "http://api.example.org/accounts/?offset=400&limit=100",
    	"previous": "http://api.example.org/accounts/?offset=200&limit=100",
    	"results": [{}]
    }

**- Add post**

POST http://127.0.0.1:8000/api/v1/posts/

**Request samples**

    Content type
    application/json
    {
        "text": "string",
        "image": "string",
        "group": 0
    }

**Response samples**

    application/json
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2019-08-24T14:15:22Z",
        "image": "string",
        "group": 0
    }

**You can find all information about endpoints here http://127.0.0.1:8000/redoc/**
