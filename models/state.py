#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


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
            cities = storage.all(City)
            cities_relation = []
            for city in cities.values():
                if city.state_id == self.id:
                    cities_relation = cities_relation.append(city)
            return cities_relation
    else:
        cities = relationship("City", backref="states",
                              cascade="delete")
