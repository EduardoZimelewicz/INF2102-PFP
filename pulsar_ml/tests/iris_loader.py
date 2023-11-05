
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

class IrisLoader:

    def setup_dataset(self):
        iris = load_iris()
        dataset = pd.DataFrame(iris.data, columns=iris.feature_names)
        dataset['target'] = iris.target
        
        return dataset

    def setup_test_train_set(self):
        dataset = self.setup_dataset()
        array = dataset.values
        X = array[:,0:4]
        Y = array[:,4]

        return train_test_split(X, Y, test_size=0.2, random_state=7)

    def setup_model(self, X_train, Y_train):
        model = RandomForestClassifier()
        model.fit(X_train, Y_train)
        
        return model

    def setup_prediction(self, X_train, X_test, Y_train):
        model = self.setup_model(X_train, Y_train)
        prediction = model.predict(X_test)
        
        return prediction
