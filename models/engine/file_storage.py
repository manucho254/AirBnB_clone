#!/usr/bin/python3
""" Class FileStorage module
"""

import json
import os
from collections import OrderedDict


class FileStorage:
    """ class that serializes instances to a JSON,
        file and deserializes JSON file to instances.
        Attributes:
                  __file_path: path to json file
                  __objects: dict to store objects by id
    """
    __file_path = "storage.json"
    __objects = {}

    def all(self) -> dict:
        """ get all objects
            Return:
                  a dictionary of objects.
        """
        return self.__objects

    def new(self, obj) -> None:
        """ set in __objects the obj with key id.
            Args:
                obj: an Object
        """
        if obj is None:
            return

        if hasattr(obj, "id"):
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self) -> None:
        """ serializes __objects to the JSON file (path: __file_path)
        """

        obj_data = OrderedDict()

        # convert all the objects to dictionaries
        for key, val in self.__objects.items():
            obj_data[key] = val.to_dict()

        # create file and add object data to json file
        with open(type(self).__file_path, "w+") as file:
            file.write("{}".format(json.dumps(obj_data)))

    def reload(self) -> None:
        """ deserializes the JSON file to __objects,
            (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised).
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if not os.path.exists(self.__file_path):
            return

        data = {}
        with open(self.__file_path, "r") as file:
            data = json.loads(file.read())

        for key, val in data.items():
            if val["__class__"] == "BaseModel":
                self.__objects[key] = BaseModel(**val)
            if val["__class__"] == "User":
                self.__objects[key] = User(**val)
            if val["__class__"] == "State":
                self.__objects[key] = Place(**val)
            if val["__class__"] == "City":
                self.__objects[key] = City(**val)
            if val["__class__"] == "Amenity":
                self.__objects[key] = Amenity(**val)
            if val["__class__"] == "Place":
                self.__objects[key] = Place(**val)
            if val["__class__"] == "Review":
                self.__objects[key] = Review(**val)
