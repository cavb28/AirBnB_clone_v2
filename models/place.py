#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id')),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id')))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # ****************************************
    amenity_ids = []

    if os.environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """FileStorage relationship between Place and Review """
            reviews = storage.all(Review)
            reviews_relation = []
            for review in reviews.values():
                if review.place_id == self.id:
                    reviews_relation = reviews_relation.append(review)
            return reviews_relation

        @property
        def amenities(self):
            """FileStorage relationship between Place and Amenity"""
            amenities = storage.all(Amenity)
            amenities_relation = []
            for amenity in amenities.values():
                if amenity.id in self.amenity_ids:
                    amenities_relation = amenities_relation.append(amenity)
            return amenities_relation

        @amenities.setter
        def amenities(self, a_id):
            """Add an amenity id for a place"""
            amenities = storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.id == a_id:
                    self.amenity_ids.append(a_id)
    else:
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref='places')
        reviews = relationship("Review", backref="places",
                               cascade="delete")
