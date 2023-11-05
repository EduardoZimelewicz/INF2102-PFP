
import pandas

class Loader:
    
    def load_data(self, dataset_csv_file_path: str, attributes: list):
        """
        Responsible for loading the dataset

        Args:
            dataset_csv_file_path(str) : Dataset file path in the csv format
            attributes(list) : List containing attributes of the dataset to add to the Dataframe
        
        Returns:
            Dataframe
                A comma-separated values (csv) file is returned as two-dimensional data structure with labeled axes.
        """
        return pandas.read_csv(dataset_csv_file_path, names=attributes)
