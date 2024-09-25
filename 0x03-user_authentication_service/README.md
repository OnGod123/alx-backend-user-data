User Authentication Service
Overview
The 0x03-user_authentication_service project provides a robust RESTful API for user authentication and session management using Flask and SQLAlchemy. The application handles user registration, login, logout, password reset, and profile retrieval, all while maintaining secure session cookies.

SQLAlchemy, an Object-Relational Mapping (ORM) tool, is used to interact with the database in a more Pythonic way, abstracting raw SQL queries and allowing seamless integration with various databases like SQLite, PostgreSQL, and MySQL.

Project Structure
graphql
Copy code
0x03-user_authentication_service/
├── app.py                # Main Flask application
├── auth.py               # Authentication logic and database interactions
├── models.py             # SQLAlchemy models for User, Sessions
├── requirements.txt      # Python dependencies
├── config.py             # Configuration settings (Database, secret keys, etc.)
└── README.md             # Project documentation
Installation
Prerequisites
Python 3.x
A database (e.g., SQLite, PostgreSQL, or MySQL)
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/your_username/alx-backend-user-data.git
cd alx-backend-user-data/0x03-user_authentication_service
Step 2: Install Dependencies
Create a virtual environment (optional but recommended) and install the required packages.

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Step 3: Configure the Database
Edit the config.py file to set up your database connection. SQLAlchemy will use this configuration to handle interactions between the application and the database.

python
Copy code
SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # Example for SQLite
# Update this line for PostgreSQL, MySQL, etc.
Step 4: Initialize the Database
Before running the app, initialize the database schema by running the following commands in Python:

bash
Copy code
python
python
Copy code
from app import db
db.create_all()
exit()
This creates the necessary tables in the database using the models defined in models.py.

Step 5: Run the Application
bash
Copy code
python app.py
The application will start on http://localhost:5000.

SQLAlchemy Integration for Authentication
SQLAlchemy provides the foundation for interacting with the database by mapping the User and Session models to tables, handling queries, and updating records.

Key SQLAlchemy Features Used:
User Model: Represents users in the database. It stores attributes like email, hashed_password, and reset_token.

Session Management: A Session model tracks user sessions by associating a session_id cookie with a specific user.

CRUD Operations: SQLAlchemy allows easy handling of create, read, update, and delete operations for users and session management. This ensures robustness when creating or managing users, logging in, updating passwords, and maintaining secure sessions.

python
Copy code
# Example User model in models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    reset_token = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return f"<User {self.email}>"
Session and Cookies
When a user logs in, a unique session ID is generated and stored as a cookie on the user's browser. This session ID is also stored in the database and linked to the corresponding user. On subsequent requests, the session ID is used to authenticate the user without the need for repeated login actions.

For example:

Session Creation: When a user logs in, a session is created and stored in both the client’s browser as a cookie and the database.
Session Validation: For routes like /profile, the session ID is retrieved from the cookie to validate the user's identity and access their data.
API Endpoints
1. Create a Session (Log In)
Endpoint: POST /sessions

Request:

bash
Copy code
curl -X POST localhost:5000/sessions -d 'email=user@example.com' -d 'password=your_password'
Response:

json
Copy code
{
    "email": "user@example.com",
    "message": "logged in"
}
A session ID is stored as a cookie in the user's browser.

2. Destroy a Session (Log Out)
Endpoint: DELETE /sessions

Request:

bash
Copy code
curl -X DELETE localhost:5000/sessions -b "session_id=your_session_id"
Response: 204 No Content

3. Get User Profile
Endpoint: GET /profile

Request:

bash
Copy code
curl -X GET localhost:5000/profile -b "session_id=your_session_id"
Response:

json
Copy code
{
    "email": "user@example.com"
}
4. Request Password Reset
Endpoint: POST /reset_password

Request:

bash
Copy code
curl -X POST localhost:5000/reset_password -d 'email=user@example.com'
Response:

json
Copy code
{
    "email": "user@example.com",
    "reset_token": "your_reset_token"
}
5. Update Password
Endpoint: PUT /reset_password

Request:

bash
Copy code
curl -X PUT localhost:5000/reset_password -d 'email=user@example.com' -d 'reset_token=your_reset_token' -d 'new_password=new_secure_password'
Response:

json
Copy code
{
    "email": "user@example.com",
    "message": "Password updated"
}
Error Handling
403 Forbidden: Returned for invalid requests, such as incorrect session IDs or reset tokens.
400 Bad Request: Returned for malformed requests.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request.

This README now includes how SQLAlchemy is used to prov