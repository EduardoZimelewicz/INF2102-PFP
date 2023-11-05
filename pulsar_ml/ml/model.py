
from sklearn.ensemble import RandomForestClassifier

class Model:

    def trainRandomForestClassifier(self, X_train: list, Y_train: list, number_of_estimators: int):
        """ 
        Random forest classifier model training

        Args:
            X_train(list): Training instances array
            Y_train(list): Training instances labels array
            number_of_estimators(int): Number of estimators

        Returns:
            self : object
                Fitted random forest classifier estimator
        """
        model = RandomForestClassifier(n_estimators=number_of_estimators)
        model.fit(X_train, Y_train)
        return model
    
    def predictRandomForestClassifier(self, model: object, X_test: list):
        """
        Random Forest Classifier prediction

        Args:
            model(object): Trained model
            X_test(list): Training instances array

        Returns:
            prediction : any
        """
        return model.predict(X_test)
