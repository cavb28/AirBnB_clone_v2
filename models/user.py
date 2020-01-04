#!/usr/bin/python3
"""User class for Airbnb Clone"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the class for user
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place", backref="users",
                          cascade="delete")

    reviews = relationship("Review", backref="users",
                           cascade="delete")
