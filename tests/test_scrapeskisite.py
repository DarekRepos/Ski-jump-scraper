"""
Module containing unit tests for the scrapeskisite module.

This module tests the functionality of the functions
in the scrapeskisite module,
including has_event_data_classes and write_event_data.

To run the tests, execute this module directly.

Example:
    To run the tests, execute the module as a script:

    python -m unittest

if you want to test interactive docstring use:

    python -m doctest -v src/scrapeskisite.py

@Author: DarekRepos
@Date: 14.03.2024
"""

import os
import unittest
from bs4 import BeautifulSoup

from src.scrapeskisite import has_event_data_classes, write_event_data


class TestSkiScraper(unittest.TestCase):
    """A class containing unit tests for the SkiScraper functions"""

    @classmethod
    def tearDownClass(cls):
        """Remove all unnecessary tests files"""
        os.remove("test_output.txt")
        os.remove("test.txt")

    def test_has_event_data_classes(self):
        """Test for has_event_data_classes function.
        - Test case with a tag containing the relevant class
        - Test case with a tag lacking the relevant class
        """
        # Test case with a tag containing the relevant class
        tag_with_class = BeautifulSoup(
            '<div class="programgl_data">Data</div>', "html.parser"
        ).find("div")
        self.assertTrue(has_event_data_classes(tag_with_class))

        # Test case with a tag lacking the relevant class
        tag_without_class = BeautifulSoup(
            '<div class="irrelevant">Data</div>', "html.parser"
        ).find("div")
        self.assertFalse(has_event_data_classes(tag_without_class))

    def test_write_event_data_programgl_data(self):
        """Test for write_event_data function with "programgl_data" node."""
        # Test case with a "programgl_data" node
        node = BeautifulSoup(
            '<div class="programgl_data">Event Data</div>', "html.parser"
        ).find("div")
        with open("test_output.txt", "w", encoding="utf-8") as file:
            write_event_data(file, node, [])  # noqa: F821
        with open("test_output.txt", "r", encoding="utf-8") as file:
            written_data = file.read()
        self.assertEqual(written_data, "Event Data ")

    def test_write_event_data_other_node(self):
        """Test for write_event_data function with other nodes containing relevant fields."""
        node = BeautifulSoup(
            """<div>
                <div class="programgl_czas">Time</div>
                <div class="programgl_impreza">Event</div>
            </div>""",
            "html.parser",
        ).find("div")
        fields = ["programgl_czas", "programgl_impreza"]
        with open("test_output.txt", "w", encoding="utf-8") as file:
            write_event_data(file, node, fields)
        with open("test_output.txt", "r", encoding="utf-8") as file:
            written_data = file.read()
        self.assertEqual(written_data, "Time|Event|")


if __name__ == "__main__":
    unittest.main()
