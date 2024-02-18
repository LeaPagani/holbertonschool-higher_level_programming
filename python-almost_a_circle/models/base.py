#!/usr/bin/python3
""" Class Base """
import json


class Base():
    """ This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs) """

    __nb_objects = 0
    """ Private class Atribute """

    def __init__(self, id=None):
        """ Class constructor
        Args:
        id(int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): a list of objects.
        """
        lst = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary (dict): The values of the wanted instance attributes.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError("Invalid class name")

        dummy_instance.update(**dictionary)  # Update dummy with dictionary
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a JSON file."""
        file_name = cls.__name__ + ".json"  # Construct the file name based on class name
        instances = []

        try:
            with open(file_name, 'r') as file:
                json_data = file.read()  # Read the JSON data from the file
                if json_data:
                    dicts = cls.from_json_string(json_data)
                    instances = [cls.create(**d) for d in dicts]
        except FileNotFoundError:
            pass  # If the file doesn't exist, return an empty list

        return instances
