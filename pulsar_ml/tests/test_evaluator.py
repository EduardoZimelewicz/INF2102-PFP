
from pulsar_ml.ml.evaluator import Evaluator
from pulsar_ml.tests.iris_loader import IrisLoader

def prediction_setup_before():
    iris = IrisLoader()

    X_train, X_test, Y_train, Y_test = iris.setup_test_train_set()

    prediction = iris.setup_prediction(X_train, X_test, Y_train)

    return prediction, Y_test

def test_ml_evaluator_accuracy():
    ml_evaluator = Evaluator()

    prediction, Y_test = prediction_setup_before()

    accuracy = ml_evaluator.evaluate_accuracy(prediction, Y_test)
    assert isinstance(accuracy, float)

def test_ml_evaluator_precision():
    ml_evaluator = Evaluator()

    prediction, Y_test = prediction_setup_before()

    precision = ml_evaluator.evaluate_precision(prediction, Y_test, average=None)
    
    assert isinstance(precision, object)

def test_ml_evaluator_recall():
    ml_evaluator = Evaluator()

    prediction, Y_test = prediction_setup_before()

    recall = ml_evaluator.evaluate_recall(prediction, Y_test, average=None)
    
    assert isinstance(recall, object)
