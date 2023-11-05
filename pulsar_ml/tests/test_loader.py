
from pulsar_ml.ml.loader import Loader

def test_load_data():
    loader = Loader()

    file_path = './pulsar_ml/tests/test_dataset.csv'
    attributes = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i'
    ]

    dataset = loader.load_data(file_path, attributes)

    assert len(dataset) == 5
