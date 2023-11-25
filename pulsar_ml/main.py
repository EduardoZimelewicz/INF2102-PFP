
import os
import pickle
from pulsar_ml.ml.loader import Loader
from pulsar_ml.ml.pre_processor import PreProcessor
from pulsar_ml.ml.model import Model
from pulsar_ml.ml.evaluator import Evaluator

def main():
    loader = Loader()
    preprocessor = PreProcessor()
    ml_model = Model()
    ml_evaluator = Evaluator()

    dataset_csv_path = 'HTRU_2.csv'
    attributes = [
        'mean',
        'standard_deviation',
        'excess_kurtosis',
        'skewness',
        'dm_snr_mean',
        'dm_snr_standard_deviation',
        'dm_snr_excess_kurtosis',
        'dm_snr_skewness',
        'class'
    ]
    test_size = 0.2

    pulsar_dataset = loader.load_data(dataset_csv_path, attributes)

    X_train, X_test, Y_train, Y_test = preprocessor.preprocess(pulsar_dataset, test_size)

    model = ml_model.trainRandomForestClassifier(X_train, Y_train, 10)

    predictions = ml_model.predictRandomForestClassifier(model, X_test)

    accuracy = ml_evaluator.evaluate_accuracy(predictions, Y_test)
    precision = ml_evaluator.evaluate_precision(predictions, Y_test, average='binary')
    recall = ml_evaluator.evaluate_recall(predictions, Y_test, average='binary')

    print("Accuracy: {}".format(accuracy))
    print("Precision: {}".format(precision))
    print("Recall: {}".format(recall))

    with open(os.path.join("./", 'random-forest-pulsar-model.pkl'), 'wb') as out:
        pickle.dump(model, out)

main()
