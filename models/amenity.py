#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from os import getenv
import sqlalchemy
from sqlalchemy import String
import models
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Represents an Amenity.

    Attributes:
        place_amenities : Place-Amenity relationship.
    """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes the Amenity class"""
        super().__init__(*args, **kwargs)
