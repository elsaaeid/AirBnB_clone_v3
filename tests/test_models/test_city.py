#!/usr/bin/python3
import unittest
import pep8
import inspect
from models.city import City
from models import storage
from models.base_model import BaseModel
import models


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_functions = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_equality_city(self):
        """Test that models/city.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings)")

    def test_pep8_equality_test_city(self):
        """Test that tests/test_models/test_city.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings)")

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(models.city.__doc__, None, "city.py needs a docstring")
        self.assertTrue(len(models.city.__doc__) >= 1, "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None, "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1, "City class needs a docstring")

    def test_city_func_docstring(self):
        """Test for the presence of docstrings in City methods"""
        for func_name, func in self.city_functions:
            self.assertIsNot(func.__doc__, None, f"{func_name} method needs a docstring")
            self.assertTrue(len(func.__doc__) >= 1, f"{func_name} method needs a docstring")


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up the test environment"""
        self.city = City()

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        self.assertIsInstance(self.city, BaseModel)
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_city_instance(self):
        """Test if City is an instance of the City class"""
        self.assertIsInstance(self.city, City)

    def test_city_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

        if models.storage_type == 'db':
            self.assertIsNone(city.name)
            self.assertIsNone(city.state_id)
        else:
            self.assertEqual(city.name, "")
            self.assertEqual(city.state_id, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attributes"""
        c = City()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in c.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))

    def test_city_save(self):
        """Test if the save function works for City"""
        self.city.name = "Test City"
        self.city.state_id = "123"
        self.city.save()
        all_cities = storage.all(City)
        city_key = "City." + self.city.id
        self.assertIn(city_key, all_cities)

    def test_city_to_dict(self):
        """Test if the to_dict function works for City"""
        city_dict = self.city.to_dict()
        self.assertEqual(self.city.__class__.__name__, 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_city_storage(self):
        """Test if City is correctly stored in the storage"""
        storage.new(self.city)
        storage.save()
        all_cities = storage.all(City)
        city_key = "City." + self.city.id
        self.assertIn(city_key, all_cities)

    def test_str(self):
        """Test that the str method has the correct output"""
        city = City()
        expected_string = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(expected_string, str(city))


if __name__ == '__main__':
    unittest.main()
