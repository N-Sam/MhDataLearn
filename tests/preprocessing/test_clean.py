import unittest

from preprocessing.clean import ------functions inside clean--------


class TestClean(unittest.TestCase):
    """
    This class provides test for all the functions inside the clean module.

    """
    def test_gender_replace(self):
        self.assertIs(df.Gender[0], "1" )

    def test_marital_replace(self):
        self.assertIs(df.MaritalStatus[0], "1" )

    def test_accom_replace(self):
        self.assertIs(df.SettledAccommodationInd[0], "1" )

    def test_employ_replace(self):
        self.assertIs(df.EmployStatus[0], "1" )