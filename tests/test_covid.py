"""This module includes a series of test cases to confirm the validity of ToolBox.py

UnitTests(unittest.TestCase) -- this class is a unit test which includes 5 different test for ToolBox.py

"""
import unittest
import pandas as pd
import matplotlib
from COVIDWA import ToolBox
import sys

sys.path.append('..')
data = pd.read_csv("data/Unemployed/Unemployment.csv")
plot_data = pd.read_csv("data/COVID19/COVID19-Rate and Unemployment.csv")


class UnitTests(unittest.TestCase):
    """"This class is a unit test which includes 8 different test for ToolBox.py."""
    #Smoke test
    def test_smoke1(self):
        """"This function is a smoke test for ToolBox.py.
        
        Args:
            self: Instance object.
        
        Returns:
            bool: True for pass the test, False otherwise.
        """
        county = "King"
        month = "June"
        text = ToolBox.unemploy_text_parser(county, month, data)

    def test_smoke2(self):
        """"This function is a smoke test for ToolBox.py.
        
        Args:
            self: Instance object.
        
        Returns:
            bool: True for pass the test, False otherwise.
        """
        county = "King"
        ToolBox.plot(county, plot_data)

    def test_oneshot1(self):
        """"This function is a smoke test for ToolBox.py.
        
        Args:
            self: Instance object.
        
        Returns:
            bool: True for pass the test, False otherwise.
        """
        county = "King"
        month = "June"
        text = ToolBox.unemploy_text_parser(county, month, data)
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
        text = ToolBox.unemploy_text_parser(county,month, data)
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
            text = ToolBox.unemploy_text_parser(county, month, data)
    
    def test_edge2(self):
        """"This function is a smoke test for ToolBox.py.
        
        Args:
            self: Instance object.
        
        Returns:
            bool: True for pass the test, False otherwise.
        """
        with self.assertRaises(ValueError):
            county = "King"
            month = "November"
            text = ToolBox.unemploy_text_parser(county, month, data)
    

if __name__ == '__main__':
    unittest.main()
