import unittest

from predict.prediction import create_prediction


class TestPrediction(unittest.TestCase):
    """
    This class will provides all the test for functions inside the prediction modules.

    """
    def test_prediction(self):

        assertEquals(type(create_prediction()), "float")
