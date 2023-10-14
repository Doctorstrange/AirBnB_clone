#!/usr/bin/python3
"""Defines the class FileStorage."""
import json
from models.base_model import BaseModel


class FileStorage:
    """ class for storing data """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        adding in __object dictionary in the format of the obj class name
        followed by "." and the id attribute of that object class
        """
        # retieve object name
        object_class_name = obj.__class__.__name__
        # store key in specified format
        key = "{}.{}".format(object_class_name, id)
        # add dicionary entry to __object
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        # initialze and store the value of the __object attribute
        dict_store = FileStorage.__objects
        # create empty dictionary to store the value of the dictionary
        obj_dict = {}
        # the object is created from the base model contaning attribute
        # the new() method sets __object with a formated dictionary represent
        # __class__.__name__.id = (name of the created object)
        # save() takes the dictionary representation
        for key in dict_store.keys():
            # extracts the value which is name of the object to save
            obj = dict_store[key]
            # uses that value as the dictionary key
            # with the result of object.to_dict() set as the key value
            obj_dict[key] = obj.to_dict()
            # open json file in write mode
        with open(FileStorage.__file_path, "w") as file:
            # dump the json represenation of the dic
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                objdict = json.load(file)
                for val in objdict.values():
                    # value would a dictionary created by to_dict()
                    cls_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(cls_name)(**val))
        except FileNotFoundError:
            return
