
import pandas as pd

class Pre_processing:
    """
    This class prepares the data berfore applying Machine Learning Algorithm
    """
    def __init__(self):
        pass

    def total_missing_values(self):
        """
        This function is used to count the total missing values in the dataset.
        ----------
        Attributes
        ----------
        data : Pandas DataFrame
            The data we want to count the total missing values.
        fill_strategies : A list of tuples, each tuple has the data to fill,
        and the axis(0 or 1)
        
        Returns
        ----------
        A new dataset after filling the missing values.
        """
        df = Pre_processing.drop(self)
        return df.isnull().sum()

    def drop(self):
        """
        This function is used to drop a column or row from the dataset.
        ----------
        Attributes
        ----------
        data : Pandas DataFrame
            The data we want to drop.
        drop_strategies : A list of tuples, each tuple has the data to drop,
        and the axis(0 or 1)
        
        Returns
        ----------
        A new dataset after dropping the unwanted data.
        """
        df = pd.read_csv("samples/test_data.csv")
        df.drop(columns=df.columns[0],
        axis=1, 
        inplace=True)
        return df

    def fill_missing_values(self):
        """
        This function is used to fill missing values in the dataset.
        ----------
        Attributes
        ----------
        data : Pandas DataFrame
            The data we want to fill missing values.
        fill_strategies : A list of tuples, each tuple has the data to fill,
        and the axis(0 or 1)
        
        Returns
        ----------
        A new dataset after filling the missing values.
        """
        df = Pre_processing.drop(self)
        cateogry_columns=df.select_dtypes(include=['object']).columns.tolist()
        integer_columns=df.select_dtypes(include=['int64','float64']).columns.tolist()
        
        for column in df:
            if df[column].isnull().any():
                if(column in cateogry_columns):
                    df[column]=df[column].fillna(df[column].mode()[0])
                else:
                    df[column]=df[column].fillna(df[column].mean)
        return df