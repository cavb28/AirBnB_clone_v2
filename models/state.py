#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os
import models

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.environ['HBNB_TYPE_STORAGE'] != 'db':
        @property
        def cities(self):
            """FileStorage relationship between State and City
            """
            cities = models.storage.all(City)
            cities_relation = []
            for city in cities.values():
                if city.state_id == self.id:
                    cities_relation.append(city)
            return cities_relation
    else:
        cities = relationship("City", backref="states",
                              cascade="delete")
