#!/usr/bin/python3
""" Class User that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ class user that defines a User
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
