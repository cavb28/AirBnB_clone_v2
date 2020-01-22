#!/usr/bin/python3
"""This is the db_storage.py File dbStorage class for AirBnB"""
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session
import os


class DBStorage:
    """This class maps instances to mySQL tables and
    mySQL tables to instances
    Attributes:
        __engine:
        __session:
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of base model class"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(os.getenv("HBNB_MYSQL_USER"),
                                                 os.getenv("HBNB_MYSQL_PWD"),
                                                 os.getenv("HBNB_MYSQL_HOST"),
                                                 os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if os.getenv("HBNB_ENV") == "test":
            meta = MetaData(self.__engine)
            meta.drop_all()

    def all(self, cls=None):
        """Method all of dbStorage class"""
        my_cls = ["State", "City", "User", "Amenity", "Place", "Review"]
        my_dict = {}
        if cls is None:
            for table in my_cls:
                query = self.__session.query(eval(table)).all()
                for obj in query:
                    key = obj.__class__.__name__ + '.' + obj.id
                    my_dict[key] = obj
        else:
            query = self.__session.query(eval(cls)).all()
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """Method new of dbStorage class"""
        if obj:
            mod_obj = obj
            self.__session.add(mod_obj)

    def save(self):
        """Method save of dbStorage class"""
        my_dict = {}
        self.__session.commit()

    def delete(self, obj=None):
        """Method delete of dbStorage class"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Method reload of dbStorage class"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        call remove() method on the private session attribute (self.__session)
        or close() on the class Session
        :return:
        """
        self.__session.close()
