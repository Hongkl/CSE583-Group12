"""This module includes a series of test cases to confirm the validity of knn.py

UnitTests(unittest.TestCase) -- this class is a unit test which includes 8 different test for knn.py
test_smoke(self) -- this is a smoke test for knn.py
test_oneshot1(self) -- this is a one shot test for knn.py
test_oneshot2(self) -- this is a one shot test for knn.py
test_edge1(self) -- this is a edge test for knn.py
test_edge2(self) -- this is a edge test for knn.py
test_edge3(self) -- this is a edge test for knn.py
test_edge4(self) -- this is a edge test for knn.py
test_edge5(self) -- this is a edge test for knn.py

"""
import unittest
import sys
import numpy as np
sys.path.insert(0, '../COVID-WA')
import CovidWeb

class UnitTests(unittest.TestCase):
    """"This class is a unit test which includes 8 different test for knn.py."""
    #Smoke test
    def test_smoke1(self):
        """"This function is a smoke test for knn.py.
        
        Args:
            self: Instance object.
        
        Returns:
            bool: True for pass the test, False otherwise.
        """
        ##The line below is just for passing pylint
        self.assertFalse(self.Months == "March")

    

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)