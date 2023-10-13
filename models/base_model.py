#!/usr/bin/python3
"""define basemodel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """the base model of the file"""

    def __init__(self, *args, **kwargs):
        """initialise instance of base model"""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__ ():
        """define string string representation of an object when it
        is converted to string"""
        class_name = __self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save():
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """return a dictionary containing all public instance attribute
        and return key __class__ as an attribute 
        """
        for key, value in self.__dict__.items(): # copy the instance attribute
            #name and as the key and its corresponding value to a dictionary
            to_dic[key] = value
        to_dic["created_at"] = self.created_at.isoformat() # copy the instance
        #attribute containing date info in isoformat
        to_dic["updated_at"] = self.updated_at.isoformat()
        to_dic["__class__"] = self.__class__.__name__
        return to_dic
