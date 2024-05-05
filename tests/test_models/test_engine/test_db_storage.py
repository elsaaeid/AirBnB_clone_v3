#!/usr/bin/python3
import unittest
import inspect
import models
from models.engine import db_storage
import pep8
from models.base_model import BaseModel
DBStorage = db_storage.DBStorage
classes = db_storage.DBStorage.classes


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation
    and style of DBStorage class
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_functions = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_equality(self):
        """Test that db_storag and
        test_db_storage.py conform to PEP8
        """
        files_to_check = ['models/engine/db_storage.py',
                          'tests/test_models/test_engine/test_db_storage.py']
        style_guide = pep8.StyleGuide()
        total_errors = 0
        error_messages = []

        for file_path in files_to_check:
            with self.subTest(path=file_path):
                result = style_guide.check_files([file_path])
                errors = result.total_errors

                if errors > 0:
                    print(f"PEP8 errors in {file_path}:")
                    for error in result.messages:
                        error_messages.append(f"- {error}")
                total_errors += errors
        if total_errors > 0:
            error_message = f"Total PEP8 errors: {total_errors}\n"
            error_message += "\n".join(error_messages)
            self.fail(error_message)

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for docstrings in DBStorage methods"""
        for func in self.dbs_functions:
            self.assertIsNot(func[1].__doc__, None,
                             f"{func[0]} method needs a docstring")
            self.assertTrue(len(func[1].__doc__) >= 1,
                            f"{func[0]} method needs a docstring")


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    @unittest.skipIf(models.storage_type != 'db',
                     "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        new_instance = BaseModel()
        models.storage.new(new_instance)
        models.storage.save()
        all_instances = models.storage.all()
        self.assertIsInstance(all_instances, dict)
        self.assertIn(new_instance, all_instances.values())

    @unittest.skipIf(models.storage_type != 'db',
                     "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all
        rows when no class is passed
        """
        new_instance = BaseModel()
        models.storage.new(new_instance)
        models.storage.save()
        all_instances = models.storage.all()
        self.assertIn(new_instance, all_instances.values())

    @unittest.skipIf(models.storage_type != 'db',
                     "not testing db storage")
    def test_new(self):
        """Test that new adds
        an object to the database
        """
        new_instance = BaseModel()
        models.storage.new(new_instance)
        models.storage.save()
        all_instances = models.storage.all()
        self.assertIn(new_instance, all_instances.values())

    @unittest.skipIf(models.storage_type != 'db',
                     "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to the db"""
        new_instance = BaseModel()
        models.storage.new(new_instance)
        models.storage.save()
        file_path = models.storage._DBStorage__engine.file_path
        with open(file_path, 'r') as file:
            data = file.read()
            self.assertIn(
                new_instance.__class__.__name__ + '.' + new_instance.id,
                data
                )

    @unittest.skipIf(models.storage_type != 'db',
                     "not testing db storage")
    def test_get(self):
        """Test that get retrieves an item in db properly"""
        new_instance = BaseModel()
        models.storage.new(new_instance)
        models.storage.save()
        retrieved_instance = models.storage.get(BaseModel,
                                                     new_instance.id)
        self.assertEqual(retrieved_instance, new_instance)

    @unittest.skipIf(models.storage_type != 'db',
                     "not testing db storage")
    def test_count(self):
        """Test that count returns the right
        number of elements in the db
        """
        initial_count = len(models.storage.all())
        new_instance = BaseModel()
        models.storage.new(new_instance)
        models.storage.save()
        updated_count = len(models.storage.all())
        self.assertEqual(updated_count, initial_count + 1)
