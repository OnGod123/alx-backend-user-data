import base64
from api.v1.auth.auth import Auth
from models.user import User  # Assuming User model is available
from typing import TypeVar

class BasicAuth(Auth):
    """ Basic authentication class inherited from Auth """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Authentication.

        Args:
            authorization_header (str): The Authorization header value.

        Returns:
            str: The Base64 part of the Authorization header if valid, else None.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, authorization_header: str) -> str:
        """ Decodes the Base64 part of the Authorization header """
        base64_str = self.extract_base64_authorization_header(authorization_header)
        if base64_str is None:
            return None
        try:
            decoded_bytes = base64.b64decode(base64_str)
            return decoded_bytes.decode('utf-8')
        except (TypeError, ValueError, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user email and password from the Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str): The Base64 decoded Authorization header.

        Returns:
            tuple: A tuple containing the user email and password, or (None, None) if invalid.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User: The authenticated User instance, or None if authentication fails.
        """
        # Validate the email and password input
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for user by email
        users = User.search({'email': user_email})  # Assuming search returns a list of users
        if not users or len(users) == 0:
            return None

        # Retrieve the user instance (assuming email is unique, so we'll take the first match)
        user = users[0]

        # Check if the password is valid
        if not user.is_valid_password(user_pwd):
            return None

        return user
