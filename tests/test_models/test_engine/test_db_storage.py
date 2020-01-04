#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


class TestFileStorage(unittest.TestCase):
    """this will test the DBStorage
    """

    @classmethod
    def setUpClass(cls):
        """set up for test
        """
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = DBStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down
        """
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in DB Storage"""
        storage = DBStorage()
        storage.reload()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        # self.assertIs(obj, storage._DBStorage__objects)

    def test_all_delete(self):
        """tests if all with filter and delete works in DB Storage
        """
        fs = DBStorage()
        fs.reload()
        # All States
        all_states = fs.all(State)
        count = len(all_states.keys())
        # Create a new State
        new_state = State()
        new_state.name = "California"
        fs.new(new_state)
        fs.save()
        # All States
        all_states = fs.all(State)
        self.assertEqual(len(all_states.keys()), count + 1)
        # Delete the new State
        fs.delete(new_state)
        # All States
        all_states = fs.all(State)
        self.assertEqual(len(all_states.keys()), count)

    def test_new(self):
        """test when new is created"""
        storage = DBStorage()
        storage.reload()
        obj = storage.all()
        user = User()
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        storage.reload()
        self.assertIsNotNone(obj[key])

    def test_reload_dbstorage(self):
        """
        tests reload
        """
        pass


if __name__ == "__main__":
    unittest.main()
