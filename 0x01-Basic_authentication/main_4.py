#!/usr/bin/env python3
""" Main 4 """
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_user_credentials(None))  # Expected output: (None, None)
print(a.extract_user_credentials(89))  # Expected output: (None, None)
print(a.extract_user_credentials("Holberton School"))  # Expected output: (None, None)
print(a.extract_user_credentials("Holberton:School"))  # Expected output: ('Holberton', 'School')
print(a.extract_user_credentials("bob@gmail.com:toto1234"))  # Expected output: ('bob@gmail.com', 'toto1234')
