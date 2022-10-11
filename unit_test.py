import unittest

from linear_regression_model import LinearRegressionModel

class TestRegressionModel(unittest.TestCase):

    def test_emptyTestValue(self):
        X = [1.0, 2.0, 3.0, 4.0]
        Y = [6.0, 5.0, 7.0, 10.0]
        Z = []
        self.assertEqual(LinearRegressionModel.cal_simple_linear_regression_coefficients(X,Y,Z), (3.5, 1.4))
        # check that there are only two returns when input Z is empty & check that they are of the correct value

    def test_regressionReturn(self):
        X = [1.0, 2.0, 3.0, 4.0]
        Y = [6.0, 5.0, 7.0, 10.0]
        Z = [2.5, 3.5]
        self.assertEqual(LinearRegressionModel.cal_simple_linear_regression_coefficients(X,Y,Z), ([7.0,8.4], 3.5, 1.4))
        # check that all returns are correct when test input is not empty

if __name__ == '__main__':
    unittest.main()