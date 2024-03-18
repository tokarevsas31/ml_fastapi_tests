import unittest
from predictor import Predictor


class Test_TestPredictor(unittest.TestCase):
    def test_predict_positive(self):
        predictor = Predictor()

        data = predictor.predict("I like machine learning!")

        assert data["label"] == "POSITIVE"

    def test_predict_negative(self):
        predictor = Predictor()

        data = predictor.predict("I hate machine learning!")

        assert data["label"] == "NEGATIVE"
