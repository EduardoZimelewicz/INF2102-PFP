
from pandas import DataFrame
from sklearn.model_selection import train_test_split

class PreProcessor:
    
    def preprocess(self, dataset, test_size, seed=7):
        """ 
        Dataset instances preprocessing (train-test instances split)

        Args:
            dataset(Dataframe) : Dataset object
            test_size(float) : Test size percentage from total instances
            seed(int) : Seed value for idempotency random numbers
        
        Returns:
           X_train : Training instances list
           X_test : Testing instances list
           Y_train : Training labels list
           Y_test : Testing labels list
        """
        X_train, X_test, Y_train, Y_test = self.__prepare_holdout(dataset, test_size, seed)
        
        return (X_train, X_test, Y_train, Y_test)
    
    def __prepare_holdout(self, dataset: DataFrame, test_size: float, seed: int):
        """ 
        Dataset instances split using holdout method

        Args:
            dataset(Dataframe): Dataset object
            test_size(float): Test size percentage from total instances
            seed(int): Seed value for idempotency random numbers
        
        Returns:
           splitting : list, length=2 * len(arrays)
                List containing train-test split of inputs
        """
        array = dataset.values
        X = array[:, 0:-1]
        Y = array[:, -1]
        return train_test_split(X, Y, test_size=test_size, random_state=seed)
