
from pulsar_ml.ml.pre_processor import PreProcessor
from pulsar_ml.tests.iris_loader import IrisLoader
import pandas as pd

def test_preprocess():
    pre_processor = PreProcessor()
    iris = IrisLoader()

    iris_dataset = iris.setup_dataset()

    test_size = 0.2

    seed = 7

    X_train, X_test, Y_train, Y_test = pre_processor.preprocess(iris_dataset, test_size, seed)

    assert len(X_train) == (len(iris_dataset) * 0.8)
    assert len(X_test) == (len(iris_dataset) * 0.2)
    assert len(Y_train) == (len(iris_dataset) * 0.8)
    assert len(Y_test) == (len(iris_dataset) * 0.2)
