#!/usr/bin/python3
"""Defines the HBnB console."""


import unittest
from time import sleep
from datetime import datetime
import os
import models
from models import storage
from models.base_model import BaseModel
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class TestBaseModel_save(unittest.TestCase):
    """to the test the save funtion of the basemodel"""

    def test_a_save(self):
        instance = BaseModel()
        sleep(0.1)
        before_save_time = instance.updated_at
        instance.save()
        self.assertLess(before_save_time, instance.updated_at)

    def test_second_save(self):
        instance = BaseModel()
        sleep(0.1)
        one_save_time = instance.updated_at
        instance.save()
        two_save_time = instance.updated_at
        instance.save()
        three_save_time = instance.updated_at
        self.assertLess(one_save_time, two_save_time)
        self.assertLess(two_save_time, three_save_time)

    def test_saveclass_id(self):
        instance = BaseModel()
        instance.save()
        class_id = "BaseModel." + instance.id
        with open("file.json", "r") as file:
            self.assertIn(class_id, file.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """to test the to_dict function in BaseModel"""

    def test_to_dict_gives_dic(self):
        instance = BaseModel()
        self.assertTrue(dict, type(instance.to_dict()))

    def test_to_dict_added_attribute(self):
        instance = BaseModel()
        instance.number = 31
        instance.name = "femi"
        self.assertIn("number", instance.to_dict())
        self.assertIn("name", instance.to_dict())

    def test_to_dict_contains_this_keys(self):
        instance = BaseModel()
        self.assertIn("id", instance.to_dict())
        self.assertIn("created_at", instance.to_dict())
        self.assertIn("updated_at", instance.to_dict())
        self.assertIn("__class__", instance.to_dict())

    def test_to_dict_no_None(self):
        instance = BaseModel()
        with self.assertRaises(TypeError):
            instance.to_dict(None)

class TestBaseModel_instance(unittest.TestCase):
    """text reaction to instance creation"""

    def test_instance_storage(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_created_at_is_datetime(self):
        instance = BaseModel()
        self.assertEqual(datetime, type(instance.created_at))

    def test_updated_at_is_datetime(self):
        instance = BaseModel()
        self.assertEqual(datetime, type(instance.updated_at))

    def test_no_args_instance(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    if __name__ == "__main__":
        unittest.main()
