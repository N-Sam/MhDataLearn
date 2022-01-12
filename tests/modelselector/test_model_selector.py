import unittest

from modelselector.model_selecter import split_data, reveal_best_classification_model


class TestModelSelecter(unittest.TestCase):

    """
    This unit test class provides all the tests for all the functions inside the model_selecter module.

    """
    def test_reveal_best_classification_model(self):
        """
        This is a test for the function reveal_best_classification_model(X_train, Y_train)
        """

        self.assertEquals(len(reveal_best_classification_model(X_train, Y_train)), 4)


    def test_split_data(self):
        """
        This is a test for the funcion split data.

        """

        self.assertEquals(len(split_data()), 4)