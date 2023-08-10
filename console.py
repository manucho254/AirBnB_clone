#!/usr/bin/python3
""" Command Line Interpreter using cmd Module """

import cmd
import json

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

""" A list of all classes """
CLASSES = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """overwrite the emptyline not to execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file,
        and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in CLASSES:
            print("** class doesn't exist **")
        else:
            obj_id = None
            if arg == "BaseModel":
                base_model = BaseModel()
                base_model.save()
                obj_id = base_model.id
            if arg == "User":
                user = User()
                user.save()
                obj_id = user.id
            if arg == "State":
                state = State()
                state.save()
                obj_id = state.id
            if arg == "City":
                city = City()
                city.save()
                obj_id = city.id
            if arg == "Amenity":
                amenity = Amenity()
                amenity.save()
                obj_id = amenity.id
            if arg == "Place":
                place = Place()
                place.save()
                obj_id = place.id
            if arg == "Review":
                review = Review()
                review.save()
                obj_id = review.id

            print(obj_id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj_dict = storage.all()
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj_dict = storage.all()
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances based
        or not on the class name"""
        args = arg.split()
        obj_dict = storage.all()
        if not args:
            obj_list = list(obj_dict.values())
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        else:
            obj_list = [
                obj for obj in obj_dict.values()
                if obj.__class__.__name__ == args[0]
            ]
        print([str(obj) for obj in obj_list])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj_dict = storage.all()
            if key not in obj_dict:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = obj_dict[key]
                attribute_name = args[2]
                attribute_value = args[3].strip("\"")
                setattr(obj, attribute_name, attribute_value)
                obj.save()

            with open("storage.json", "r") as file:
                print(file.read())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
