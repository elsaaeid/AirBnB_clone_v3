#!/usr/bin/python3
import console
import pep8
import unittest
from io import StringIO

from unittest.mock import patch
from console import HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_equality(self):
        """Test that console.py and test_console.py conform to PEP8"""
        files_to_check = ['console.py',
                          'tests/test_console.py']
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

    def test_console_module_docstring(self):
        """Test for the console.py module"""
        self.assertIsNot(
            console.__doc__,
            None,
            "console.py needs a docstring"
        )
        self.assertTrue(
            len(console.__doc__) >= 1,
            "console.py needs a docstring"
        )

    def test_console_class_docstring(self):
        """Test for the class console"""
        self.assertIsNot(
            HBNBCommand.__doc__,
            None,
            "HBNBCommand class needs a docstring"
        )
        self.assertTrue(
            len(HBNBCommand.__doc__) >= 1,
            "HBNBCommand class needs a docstring"
        )


class TestConsole(unittest.TestCase):
    """Class to test methods of console commands"""
    @classmethod
    def setUpClass(cls):
        """Create command console to test with"""
        cls.cmdcon = HBNBCommand()

    def setUp(self):
        """Create in memory buffer"""
        self.output = StringIO()

    def tearDown(self):
        """Close in memory buffer"""
        self.output.close()

    def assert_stdout(self, command, expected_output):
        """Helper method to assert the captured
        stdout matches the expected output
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd(command)
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_base_model_all(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("BaseModel.all()")
            self.assertIn("[BaseModel]", f.getvalue())

    def test_base_model_count(self):
        """Test the "count" command for BaseModel"""
        expected_output = "7"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("BaseModel.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_base_model_show(self):
        """Test the "show" command for BaseModel"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("BaseModel.show()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_base_model_destroy(self):
        """Test the "destroy" command for BaseModel"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("BaseModel.destroy()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_base_model_update(self):
        """Test the "update" command for BaseModel"""
        expected_output = "Invalid update command format"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("BaseModel.update()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    # def test_amenity_all(self):
    #     """Test the all command"""
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         self.cmdcon.onecmd("Amenity.all()")
    #         self.assertIn("Amenity", f.getvalue())

    def test_amenity_count(self):
        """Test the "count" command for Amenity"""
        expected_output = "6"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("count Amenity")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_amenity_show(self):
        """Test the "show" command for Amenity"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("show Amenity")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_amenity_destroy(self):
        """Test the "destroy" command for Amenity"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("destroy Amenity")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_amenity_update(self):
        """Test the "update" command for Amenity"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("update Amenity")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_city_all(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("City.all()")
            self.assertIn("[City]", f.getvalue())

    def test_city_count(self):
        """Test the "count" command for City"""
        expected_output = "4"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("City.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_city_show(self):
        """Test the "show" command for City"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("City.show()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_city_destroy(self):
        """Test the "destroy" command for City"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("City.destroy()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_city_update(self):
        """Test the "update" command for City"""
        expected_output = "Invalid update command format"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("City.update()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_place_all(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("Place.all()")
            self.assertIn("[Place]", f.getvalue())

    def test_place_count(self):
        """Test the "count" command for Place"""
        expected_output = "9"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("Place.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_place_show(self):
        """Test the "show" command for Place"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("Place.show()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_place_destroy(self):
        """Test the "destroy" command for Place"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("Place.destroy()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_place_update(self):
        """Test the "update" command for Place"""
        expected_output = "Invalid update command format"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("Place.update()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_review_all(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("Review.all()")
            self.assertIn("[Review]", f.getvalue())

    def test_review_count(self):
        """Test the "count" command for Review"""
        expected_output = "6"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("Review.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_review_show(self):
        """Test the "show" command for Review"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("Review.show()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_review_destroy(self):
        """Test the "destroy" command for Review"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("Review.destroy()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_review_update(self):
        """Test the "update" command for Review"""
        expected_output = "Invalid update command format"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("Review.update()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_state_all(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("State.all()")
            self.assertIn("[State]", f.getvalue())

    def test_state_count(self):
        """Test the "count" command for State"""
        expected_output = "12"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("State.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_state_show(self):
        """Test the "show" command for State"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("State.show()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_state_destroy(self):
        """Test the "destroy" command for State"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("State.destroy()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_state_update(self):
        """Test the "update" command for State"""
        expected_output = "Invalid update command format"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("State.update()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_user_all(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("User.all()")
            self.assertIn("[User]", f.getvalue())

    def test_user_count(self):
        """Test the "count" command for User"""
        expected_output = "13"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("User.count()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_user_show(self):
        """Test the "show" command for User"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("User.show()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_user_destroy(self):
        """Test the "destroy" command for User"""
        expected_output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("User.destroy()")
            self.assertEqual(f.getvalue().strip(), expected_output)

    def test_user_update(self):
        """Test the "update" command for User"""
        expected_output = "Invalid update command format"
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmdcon.onecmd("User.update()")
            self.assertEqual(f.getvalue().strip(), expected_output)
