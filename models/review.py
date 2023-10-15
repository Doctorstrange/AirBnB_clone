#!/usr/bin/python3
"""Defines Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent one review"""

    place_id = ""
    user_id = ""
    text = ""

