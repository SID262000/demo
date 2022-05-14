
class Pre_processing:
    """
    This class prepares the data berfore applying Machine Learning Algorithm
    """
    def __init__(self):
        
        print()
        print('pre-processing object is created')
        print()    
    
    def drop(self, data, drop_strategies):
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
        
        self.data=data
        
        for columns, ax in drop_strategies:
            if len(columns)==1:
                self.data=self.data.drop(labels=column, axis=ax)
            else:
                for column in columns:
                    self.data=self.data.drop(labels=column, axis=ax)
        return self.data

    def fillna(self, ntrain, fill_strategies):       
        """
        This function fills NA/NaN values in a specific column using a specified method(zero,mean,
        mode,median)
        
        ---------
        Attributes
        ----------
        data : Pandas DataFrame
            The data whose missing values we want to impute
        fill_strategies : A dictionary, its keys represent the columns, 
        and the values represent the value to use to fill the Nulls.
        
        Returns
        ----------
        A new dataset without null values.
        """
        def fill(column, fill_with):
            
                if str(fill_with).lower() in ['zero', 0]:
                    self.data[column].fillna(0, inplace=True)
                elif str(fill_with).lower()=='mode':
                    self.data[column].fillna(self.data[column].mode()[0], inplace=True)
                elif str(fill_with).lower()=='mean':
                    self.data[column].fillna(self.data[column].mean(), inplace=True)
                elif str(fill_with).lower()=='median':
                    self.data[column].fillna(self.data[column].median(), inplace=True)
                else:
                    self.data[column].fillna(fill_with, inplace=True)

                return self.data

        #imputing columns according to its strategy
        for columns, strategy in fill_strategies:
            if len(columns)==1:
                fill(columns[0], strategy)
            else:
                for column in columns:
                    fill(column, strategy)

        return self.data
    
 
        def feature_engineering(self):
            """
            This function is used to apply some feature engineering on the data.
            ----------
            Attributes
            ----------
            data : Pandas DataFrame
            The data on which we want to apply feature engineering.
        
            Returns
            ----------
            A new dataset with new columns and some additions.
            """
        # creating new columns
        self.data['TotalSF'] = self.data['TotalBsmtSF'] + self.data['1stFlrSF'] + self.data['2ndFlrSF']
                
        # Convert some columns from numeric to string
        self.data[['YrSold','MSSubClass','MoSold','OverallCond']] = self.data[['YrSold','MSSubClass','MoSold','OverallCond']].astype(str)
        
        # Convert some columns from numeric to int
        self.data[['BsmtHalfBath','BsmtFinSF1', 'BsmtFinSF2','BsmtFullBath','BsmtUnfSF','GarageCars','GarageArea']]\
        =self.data[['BsmtHalfBath','BsmtFinSF1', 'BsmtFinSF2','BsmtFullBath','BsmtUnfSF','GarageCars','GarageArea']].astype(int)

        return self.data    
        
   
    def label_encoder(self, columns):
        """
        This function is used to encode the data to categorical values to benefit from increasing or 
        decreasing to build the model    
        ----------
        Attributes
        ----------
        data : Pandas DataFrame
            The data we want to encode.
        columns : columns to convert.
        
        Returns
        ----------
        A dataset without categorical data.
        """

        # Convert all categorical collumns to numeric values
        lbl = LabelEncoder() 
        
        self.data[columns] = self.data[columns].apply(lambda x:lbl.fit_transform(x.astype(str)).astype(int))
        
        return self.data 
    
    def get_dummies(self, columns):
        """
        This function is used to convert the data to dummies values.
        ----------
        Attributes
        ----------
        data : Pandas DataFrame
            The data we want to convert.
        
        Returns
        ----------
        A dataset with dummies.
        """
        
        # convert our categorical columns to dummies
        for col in columns:
            dumm = pd.get_dummies(self.data[col], prefix = col, dtype=int)
            self.data = pd.concat([self.data, dumm], axis=1)

        self.data.drop(columns, axis=1, inplace=True)
        
        return self.data
        
    def norm_data(self, columns):
        """
        This function is used to normalize the data.   
        ----------
        Attributes
        ----------
        data : Pandas DataFrame
            The data we want to normalize.
        
        Returns
        ----------
        A new normalized dataset.
        """
        
        # Normalize our numeric data
        self.data[columns] = self.data[columns].apply(lambda x:np.log1p(x)) #Normalize the data with Logarithms
        
        return self.data
              