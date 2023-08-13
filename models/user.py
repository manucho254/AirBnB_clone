#!/usr/bin/python3
""" module for implementation of User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ class User that defines a User.
        Attributes:
                  email: user email
                  password: user password
                  first_name: first_name
                  last_name: last name of user
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
