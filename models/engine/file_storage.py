#!/usr/bin/python3
""" Class FileStorage module
"""

import json
import os
from datetime import datetime


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
            self.__objects[key] = obj.to_dict()

    def save(self) -> None:
        """ serializes __objects to the JSON file (path: __file_path)
        """

        to_json = json.dumps(self.__objects)

        with open(type(self).__file_path, "w+") as file:
            file.write("{}".format(to_json))

    def reload(self) -> None:
        """ deserializes the JSON file to __objects,
            (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised).
        """

        if not os.path.exists(type(self).__file_path):
            return

        with open(type(self).__file_path, "r") as file:
            data = file.read()
            self.__objects = json.loads(data)
