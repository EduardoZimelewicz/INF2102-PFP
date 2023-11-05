

from sklearn.metrics import precision_score, recall_score, accuracy_score

class Evaluator:

    def evaluate_accuracy(self, prediction: any, Y_test: list):
        """ 
        Model prediction accuracy evaluation

        Args:
            prediction(any): Model prediction values
            Y_test(list): Testing instances labels array

        Returns:
            accuracy_score : float
                Model accuracy result
        """
        return accuracy_score(Y_test, prediction)

    def evaluate_precision(self, prediction: any, Y_test: list, average: str):
        """ 
        Model precision evaluation

        Args:
            prediction(any): Model prediction values
            Y_test(array): Testing instances labels array
            average(str): Label definition type

        Returns:
            precision_score : float
                Model recall result
        """
        return precision_score(Y_test, prediction, average=average)
    
    def evaluate_recall(self, prediction: any, Y_test: list, average: str):
        """ 
        Model recall evaluation

        Args:
            prediction(any): Model prediction values
            Y_test(array): Testing instances labels array
            average(str): Label definition type

        Returns:
            recall_score : float
                Model recall result
        """
        return recall_score(Y_test, prediction, average=average)
