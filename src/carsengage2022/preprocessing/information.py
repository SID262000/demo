
class Information:
    """
    This class shows some information about the dataset

    """
    def __init__(self):
        
        print()
        print('Information object is created')
        print()
        
    def get_missing_values(self, data):
        """
        This function finds the missing values in the dataset

        ----------
        Attributes
        ----------
        data : Pandas DataFrame
        The data whose information we want to see
        
        Returns
        ----------
        A Pandas Series contains the missing values in descending order
        """
        #get the sum of all missing values in the dataset
        missing_values = data.isnull().sum()
        #sorting the missing values in a pandas Series
        missing_values = missing_values.sort_values(ascending=False)
        
        #returning the missing values Series
        return missing_values
    
    def _info_(self, data):
        """
        This function shows some information about the data like 
        Feature names,data type, number of missing values for each feature 
        and ten samples of each feature

        ----------
        Attributes
        ----------
        data : Pandas DataFrame
            The data whose information we want to see
        
        Returns
        ----------
        Information about the DataFrame

        """
        self.data=data
        feature_dtypes=self.data.dtypes
        feature_info=self.data.info
        self.missing_values=self.get_missing_values(self.data)
        feature_names=self.missing_values.index.values
        missing_values=self.missing_values.values
        rows, columns=data.shape

        print("-" * 50)
        print('This data contains {} rows and {} columns'.format(rows,columns))
        print("-" * 50)
        print()
        
        print("{:13} {:13} {:30} {:15}".format('Feature Name'.upper(),
                                               'Data Format'.upper(),
                                               'Null values(Num-Perc)'.upper(),
                                               'Seven Samples'.upper()))
        for feature_name, dtype, missing_value,feature_info in zip(feature_names,feature_dtypes[feature_names],missing_values,feature_info):
            print("{:15} {:14} {:20}".format(feature_name,
                                             str(dtype), 
                                             str(missing_value) + ' - ' + 
                                             str(round(100*missing_value/sum(self.missing_values),3))+' %'),
                                             feature_info, end="")

            for i in np.random.randint(0,len(data),7):
                print(data[feature_name].iloc[i], end=",")
            print()

        print("-"*50)
        