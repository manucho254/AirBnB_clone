#!/usr/bin/python3
""" Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ class Review that defines a review.
        Attributes:
                  place_id: a place id, it will be the Place.id.
                  user_id: a user id, it will be the User.id.
                  text: the review text.
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
