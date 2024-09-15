from typing import List, TypeVar
from flask import request

class Auth:
    """
    Template class for managing API authentication.
    """
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a given path requires authentication.
        
        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require authentication.

        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        if path is None:
            return True
        
        if not excluded_paths or len(excluded_paths) == 0:
            return True

        # Add a trailing slash to the path if it doesn't exist for comparison
        if not path.endswith('/'):
            path += '/'

        # Check if the path matches any path in excluded_paths
        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                # If both paths match, return False (no authentication required)
                if path == excluded_path:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the Authorization header from the request.
        
        Args:
            request (Flask request): The Flask request object.

        Returns:
            str: None for now, but logic will be added later.
        """""" Return the authorization header from the request """
        
        if request is None:
            return None
        return request.headers.get('Authorization', None)
        

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request.
        
        Args:
            request (Flask request): The Flask request object.

        Returns:
            User: None for now, but logic will be added later.
        """
        return None
