# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

Basic Authentication API
This project is an implementation of Basic Authentication for an API built with Flask. The API protects certain routes, requiring users to authenticate using Basic Authentication. The user credentials are validated against a stored user database, and the project follows REST principles to provide secure access to user data.

Table of Contents
Project Overview
Requirements
Directory Structure
Installation
Basic Authentication Flow
Usage
Testing
API Endpoints
Examples
Project Overview
This project provides a secure Basic Authentication mechanism for accessing protected resources within the API. It handles:

Extracting the Authorization header.
Decoding the Base64 credentials.
Validating the credentials against a user database.
Granting or denying access based on authentication success.
The authentication is implemented in a Python class BasicAuth that inherits from the Auth base class, and includes methods to handle authentication logic.

Requirements
Python 3.x
Flask
Basic knowledge of REST APIs and authentication
User model implementation for user management
Directory Structure
markdown
Copy code
.
├── api
│   └── v1
│       ├── __init__.py
│       ├── app.py
│       └── auth
│           ├── __init__.py
│           ├── auth.py
│           └── basic_auth.py
├── models
│   └── user.py
├── main_6.py
└── README.md
Key Files:
api/v1/auth/basic_auth.py: Implements the BasicAuth class that handles all the Basic Authentication logic.
models/user.py: The user model with attributes like email, password, and methods to verify passwords.
main_6.py: Script to create a user for testing the authentication mechanism.
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/OnGod123/alx-backend-user-data.git
cd alx-backend-user-data/0x01-Basic_authentication
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask API:

bash
Copy code
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
Basic Authentication Flow
Authorization Header:

The client sends an Authorization header in the format: Basic <Base64-encoded-credentials>.
Base64 Decoding:

The BasicAuth class extracts the Base64 string from the header, decodes it to retrieve the user credentials in the format email:password.
User Authentication:

The credentials are split and validated against the user data stored in the database. The password is hashed and checked for validity.
Access Control:

If authentication is successful, access to protected resources is granted. Otherwise, the API responds with appropriate error messages like "Unauthorized" or "Forbidden".
Usage
To test the functionality, follow these steps:

Create a new user: Run the main_6.py script to create a user with a specified email and password.

bash
Copy code
python3 main_6.py
This script will:

Create a new user with the credentials bob@hbtn.io and H0lbertonSchool98!.
Print the Base64-encoded string for these credentials.
Start the API:

bash
Copy code
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
Testing
Use curl commands to test the API.

Without Authentication:
bash
Copy code
curl "http://0.0.0.0:5000/api/v1/status"
Response:

json
Copy code
{
  "status": "OK"
}
Protected Route (Unauthorized):
bash
Copy code
curl "http://0.0.0.0:5000/api/v1/users"
Response:

json
Copy code
{
  "error": "Unauthorized"
}
With Invalid Authorization Header:
bash
Copy code
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
Response:

json
Copy code
{
  "error": "Forbidden"
}
With Valid Authorization Header:
bash
Copy code
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
Response:

json
Copy code
[
  {
    "created_at": "2023-09-14T12:00:00", 
    "email": "bob@hbtn.io", 
    "first_name": null, 
    "id": "9375973a-68c7-46aa-b135-29f79e837495", 
    "last_name": null, 
    "updated_at": "2023-09-14T12:00:00"
  }
]
API Endpoints
/api/v1/status: Returns the status of the API (no authentication required).
/api/v1/users: Returns a list of users (requires Basic Authentication).
Examples
Creating a new user and generating Base64 credentials:

bash
Copy code
python3 main_6.py
Example output:

sql
Copy code
New user: 9375973a-68c7-46aa-b135-29f79e837495 / bob@hbtn.io
Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
Making an authenticated request:

bash
Copy code
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
Conclusion
This project demonstrates how to implement Basic Authentication in a Python-based API using Flask. The BasicAuth class is responsible for extracting and decoding credentials from the Authorization header and validating users. The authentication ensures secure access to protected resources by checking user credentials against a stored database of users.

Enjoy working with secure APIs!



