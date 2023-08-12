#!/usr/bin/python3
""" City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ class City that defines a city.
        Attributes:
                  state_id: a state id, it will be the State.id.
                  name: name of the city
    """
    state_id: str = ""
    name: str = ""
