#!/usr/bin/python3
""" test amenity function """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """class amenity function """

    def __init__(self, *args, **kwargs):
        """ innitialization test"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test name innitialization """
        new = self.value()
        self.assertEqual(type(new.name), str)
