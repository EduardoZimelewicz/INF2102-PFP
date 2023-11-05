
from pulsar_ml.ml.model import Model
from pulsar_ml.tests.iris_loader import IrisLoader
from sklearn.ensemble import RandomForestClassifier

def test_ml_model_train():
    ml_model = Model()
    iris = IrisLoader()

    X_train, X_test, Y_train, Y_test = iris.setup_test_train_set()

    n_estimators = 10

    model = ml_model.trainRandomForestClassifier(X_train, Y_train, n_estimators)

    assert isinstance(model, RandomForestClassifier)

def test_ml_model_predict():
    ml_model = Model()
    iris = IrisLoader()
    
    X_train, X_test, Y_train, Y_test = iris.setup_test_train_set()

    model = iris.setup_model(X_train, Y_train)

    model_predicted = ml_model.predictRandomForestClassifier(model, X_test)

    assert isinstance(model_predicted, object)
