#!/usr/bin/python3
"""define basemodel class"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """the base model of the file"""

    def __init__(self, *args, **kwargs):
        """initialise instance of base model"""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs != 0:
            for key, arg in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(arg, date_format)
                else:
                    self.__dict__[key] = args
        else:
            models.storage.new(self)

    def __str__(self):
        """define string string representation of an object when it
        is converted to string"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save():
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """return a dictionary containing all public instance attribute
        and return key __class__ as an attribute 
        """
        to_dic = self.__dict__.copy()
        to_dic["created_at"] = self.created_at.isoformat() # copy the instance
            #attribute containing date info in isoformat
        to_dic["updated_at"] = self.updated_at.isoformat()
        to_dic["__class__"] = self.__class__.__name__
        return to_dic

    
