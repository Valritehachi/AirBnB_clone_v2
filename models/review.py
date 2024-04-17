#!/usr/bin/python3
""" Review module for the HBNB project """

from models.base_model import Base
from models.base_model import BaseModel
import models
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from os import getenv
from sqlalchemy import String
from sqlalchemy.orm import relationship
import sqlalchemy


class Review(BaseModel, Base):
    """ Review class to store review information """
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes the review class"""
        super().__init__(*args, **kwargs)
