"""This module includes a series of test cases to confirm the validity of knn.py

UnitTests(unittest.TestCase) -- this class is a unit test which includes 8 different test for knn.py

"""
import unittest
import sys
import numpy as np
sys.path.insert(0, '../COVID-WA')
import ToolBox

class UnitTests(unittest.TestCase):
    """"This class is a unit test which includes 8 different test for knn.py."""
    #Smoke test
    def test_smoke(self):
        """"This function is a smoke test for ToolBox.py.
        
        Args:
            self: Instance object.
        
        Returns:
            bool: True for pass the test, False otherwise.
        """
        county = "King"
        month = "June"
        text = ToolBox.unemploy_text_parser(county,month)

    def test_oneshot1(self):
        """"This function is a smoke test for ToolBox.py.
        
        Args:
            self: Instance object.
        
        Returns:
            bool: True for pass the test, False otherwise.
        """
        county = "King"
        month = "June"
        text = ToolBox.unemploy_text_parser(county,month)
        test_text = 'County Name: King County     Period: June     Unemployment Rate: 9.6'
        self.assertEqual(text, test_text)
    
    def test_oneshot2(self):
        """"This function is a smoke test for ToolBox.py.
        
        Args:
            self: Instance object.
        
        Returns:
            bool: True for pass the test, False otherwise.
        """
        county = "Pacific"
        month = "September"
        text = ToolBox.unemploy_text_parser(county,month)
        test_text = 'County Name: Pacific County     Period: September     Unemployment Rate: 9.5'
        self.assertEqual(text, test_text)
    
    def test_edge1(self):
        """"This function is a smoke test for ToolBox.py.
        
        Args:
            self: Instance object.
        
        Returns:
            bool: True for pass the test, False otherwise.
        """
        with self.assertRaises(ValueError):
            county = "San Francisco"
            month = "June"
            text = ToolBox.unemploy_text_parser(county,month)
    
    def test_edge1(self):
        """"This function is a smoke test for ToolBox.py.
        
        Args:
            self: Instance object.
        
        Returns:
            bool: True for pass the test, False otherwise.
        """
        with self.assertRaises(ValueError):
            county = "King"
            month = "November"
            text = ToolBox.unemploy_text_parser(county,month)
    

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)