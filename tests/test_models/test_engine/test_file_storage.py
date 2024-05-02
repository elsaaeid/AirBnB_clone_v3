#!/usr/bin/python3
import unittest
import inspect
import models
from models.engine import file_storage
from models.base_model import BaseModel
import json
import pep8
storage = models.storage
from models.engine.file_storage import FileStorage
classes = FileStorage.classes


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and
    style of FileStorage class
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_functions = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_equality(self):
        """Test that file_storage.py
        test_file_storage.py nad conform to PEP8"""
        files_to_check = ['models/engine/file_storage.py',
                          'tests/test_models/test_engine/test_file_storage.py']
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

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class needs a docstring")

    def test_fs_func_docstrings(self):
        """Test for the presence of docstrings in FileStorage methods"""
        for func in self.fs_functions:
            self.assertIsNot(func[1].__doc__, None,
                             f"{func[0]} method needs a docstring")
            self.assertTrue(len(func[1].__doc__) >= 1,
                            f"{func[0]} method needs a docstring")

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    def setUp(self):
        """Test initialization"""
        self.storage = FileStorage()
        self.storage.__objects = {}

    @unittest.skipIf(models.storage_type == 'db', "not testing file storage")
    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage.__objects)

    @unittest.skipIf(models.storage_type == 'db', "not testing file storage")
    def test_new(self):
        """Test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage.__objects
        FileStorage.__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = f"{instance.__class__.__name__}.{instance.id}"
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage.__objects)
        FileStorage.__objects = save

    @unittest.skipIf(models.storage_type == 'db', "not testing file storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = f"{instance.__class__.__name__}.{instance.id}"
            new_dict[instance_key] = instance
        save = FileStorage.__objects
        FileStorage.__objects = new_dict
        storage.save()
        FileStorage.__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))

    @unittest.skipIf(models.storage_type == 'db', "not testing file storage")
    def test_get_and_count(self):
        """Test that get retrieves objects stored in file.json and
        count returns the right number of objects"""
        new_instance = BaseModel()
        models.storage_type.new(new_instance)
        models.storage_type.save()
        instance_key = f"{new_instance.__class__.__name__}.{new_instance.id}"
        retrieved_instance = models.storage_type.get(BaseModel, instance_key)
        self.assertEqual(new_instance, retrieved_instance)
        self.assertEqual(models.storage_type.count(),
                         len(models.storage_type.all()))
