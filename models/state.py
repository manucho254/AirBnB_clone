#!/usr/bin/python3
""" State class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """ class State that defines a state
        Attributes:
                  name: name of the state
    """
    name: str = ""
