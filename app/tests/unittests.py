import unittest
import json
import os
from app.main import load_json


# Define a test class that inherits from unittest.TestCase
class TestLoadJson(unittest.TestCase):
    # Define a setUp method to create a temporary JSON file for testing
    def setUp(self):
        self.temp_json_file = 'temp_test.json'
        with open(self.temp_json_file, 'w') as file:
            json.dump({'key': 'value'}, file)

    # Define a tearDown method to clean up the temporary JSON file
    def tearDown(self):
        os.remove(self.temp_json_file)

    # Define a test method to check if load_json loads JSON correctly
    def test_load_json_valid(self):
        data = load_json(self.temp_json_file)
        self.assertEqual(data, {'key': 'value'})

    # Define a test method to check if load_json handles invalid JSON files
    def test_load_json_invalid(self):
        with open(self.temp_json_file, 'w') as file:
            file.write("Invalid JSON")
        with self.assertRaises(Exception):
            load_json(self.temp_json_file)

    # Define a test method to check if load_json handles missing files
    def test_load_json_missing_file(self):
        non_existent_file = 'non_existent.json'
        with self.assertRaises(Exception):
            load_json(non_existent_file)


if __name__ == '__main__':
    unittest.main()
