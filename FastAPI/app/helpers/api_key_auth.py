"""
API Key Authentication Module

This module implements a basic API key authentication system for a FastAPI application. 
It uses the `APIKeyHeader` from FastAPI's security module and validates the key against 
an environment variable `API_KEY`.

Dependencies:
- fastapi: Provides the web framework and HTTP exception handling.
- fastapi.security.api_key: Provides the API key security implementation.
- os: Used to interact with environment variables.
- dotenv: Loads environment variables from a `.env` file.

The `get_api_key` function validates the provided API key in the request header 
against the predefined key from the environment. If the keys don't match, a 403 
Forbidden error is raised.
"""

import os
from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv

# Load environment variables from a .env file.
load_dotenv()

# Fetch the API key from environment variables.
API_KEY = os.getenv("API_KEY")
API_KEY_NAME = API_KEY

# Define the API key header object with the name of the key fetched from the environment.
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    """
    Verifies the provided API key in the request header.

    Args:
        api_key_header (str): The API key passed in the request header.

    Returns:
        str: The validated API key if it matches the expected key.

    Raises:
        HTTPException: If the API key is invalid or missing, returns a 403 error with a custom message.
    """
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "status": "False",
                "status_code": status.HTTP_403_FORBIDDEN,
                "message": "Unauthorized",
            },
        )
