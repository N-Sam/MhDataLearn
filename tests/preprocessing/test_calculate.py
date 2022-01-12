import unittest

from preprocessing.calculate import ------functions inside calculate--------

class TestCalculate(unittest.TestCase):
    """
    This class will proivdes all the test for the calculate module.

    """
    def test_calc_age_admit(self):

        self.assertEquals(type(calc_age_admit(df)), "pandas.core.dataframe" )


    def test_check_emergency(self):
        """
        This is a test for the function check emergency
        """
        self.assertEquals("Emergency" in check_emergency(df).columns)


    def test_emergency_readmit(self):
        """
        This is a test for the function emergency readmit
        """
        self.assertIn("EmergencyReadmit", check_emergency(df).columns)

    
    def test_postcode_to_lsoa(self):
        """
        This is a test for the function postcode to lsoa
        """
        self.assertIn("lsoa", check_emergency(df).columns)

    
    def test_lsoa_to_imd(self):
        """
        This is a test for the function lsoa to imd
        """
        self.assertIn("imd_decile", check_emergency(df).columns)