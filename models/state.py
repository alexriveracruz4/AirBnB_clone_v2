#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
    name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """
            returns the list of City instances with state_id equals
            to the current State.id
            """
            list_city = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
