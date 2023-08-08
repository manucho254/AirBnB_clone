#!/usr/bin/python3
""" Base model class module
"""

from uuid import uuid4
from datetime import datetime


CURRENT_DATE = datetime.now()


class BaseModel:
    """ BaseModel that defines all common,
        attributes/methods for other classes.
    """
    def __init__(self) -> None:
        """ method to initalize class BaseModel
        """
        self.id = uuid4()
        self.created_at = CURRENT_DATE
        self.updated_at = CURRENT_DATE

    def __str__(self) -> str:
        """ get string respresentation of class BaseModel.
            Return:
                  string represtation of BaseModel.
        """
        class_name = self.__class__.__name__
        return "[{0}] ({1}) <{2}>".format(class_name, self.id, self.__dict__)

    def save(self) -> None:
        """ update public instance updated_at
        """
        self.updated_at = CURRENT_DATE

    def to_dict(self) -> dict:
        """ get and return all keys/values of __dict__
           Return:
                 a dictionary containing all,
                 keys/values of __dict__ of the instance.
        """
        base_dict = self.__dict__
        base_dict["created_at"] = self.__to_string(base_dict["created_at"])
        base_dict["updated_at"] = self.__to_string(base_dict["updated_at"])
        base_dict["__class__"] = self.__class__.__name__

        return base_dict

    def __to_string(self, date: datetime) -> str:
        """ convert datetime object to string in ISO format
            Return:
                  string represetation of datetime object in ISO format.
        """
        return date.isoformat()
