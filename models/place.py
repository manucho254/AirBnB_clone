#!/usr/bin/python3
""" Place class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ class Place that defines a place.
        Attributes:
                  city_id: the city id, it will be the City.id
                  user_id: the user id, it will be the User.id
                  name: name of place.
                  description: a description for place.
                  number_rooms: number of rooms
                  number_bathrooms: number of bathroooms
                  max_guest: maximum number of guests
                  price_by_night: price per night
                  latitude: latitude value
                  longitude: longitude value
                  amenity_ids: list of amenity ids, ["Amenity.id",]

    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float - 0.0
    longitude: float = 0.0
    amenity_ids: list = []
