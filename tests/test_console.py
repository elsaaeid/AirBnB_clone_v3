#!/usr/bin/python3
import console
import pep8
import unittest
HBNBCommand = console.HBNBCommand


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
