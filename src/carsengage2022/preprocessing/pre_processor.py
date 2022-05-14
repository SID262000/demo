
class Preprocessor:
    
    def __init__(self):
        self.data=None
        self._preprocessor=Pre_processing()

    def _process(self, data, ntrain):

        self.data=data
        
        self.ntrain=ntrain
        
        cols_drop=['Utilities', 'OverallQual','TotRmsAbvGrd']
        
        # Numeric columns
        num_cols = ['LotFrontage','LotArea','YearBuilt','YearRemodAdd','MasVnrArea',
                    'BsmtFinSF1','BsmtFinSF2','BsmtUnfSF','TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 
                    'LowQualFinSF','GrLivArea','BsmtFullBath','BsmtHalfBath','FullBath','HalfBath', 
                    'BedroomAbvGr','KitchenAbvGr','Fireplaces','GarageYrBlt','GarageCars','GarageArea', 
                    'WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch','PoolArea','MiscVal']

        # Categorical columns
        cat_cols = ['MSSubClass','MSZoning','Street','Alley','LotShape','LandContour','LotConfig','LandSlope', 
                    'Neighborhood','Condition1','Condition2','BldgType','HouseStyle','RoofStyle','RoofMatl', 
                    'Exterior1st','Exterior2nd','MasVnrType','ExterQual','ExterCond','Foundation','BsmtQual', 
                    'BsmtCond','BsmtExposure','BsmtFinType1','BsmtFinType2','Heating','HeatingQC','CentralAir', 
                    'Electrical','KitchenQual','Functional','FireplaceQu','GarageType','GarageFinish', 
                    'GarageQual','GarageCond','PavedDrive','PoolQC','Fence','MiscFeature','MoSold','SaleType', 
                    'SaleCondition','OverallCond', 'YrSold']
        
        drop_strategies=[(cols_drop,1)]

        fill_strategies=[(['BsmtFinType2','BsmtQual','BsmtCond','ExterQual','ExterCond','MasVnrArea',
                          'TotalBsmtSF','HeatingQC','BsmtHalfBath','BsmtFinSF1','BsmtFinSF2','GarageYrBlt',
                          'BsmtFullBath','BsmtUnfSF','GarageCars','GarageArea','MasVnrArea'],0),
                         (['FireplaceQu','GarageQual','GarageCond','BsmtFinType1','MasVnrType',
                          'BsmtExposure','GarageFinish','PoolQC','Fence','LandSlope','GarageType',
                          'LotShape','PavedDrive','Street','Alley','CentralAir','MiscFeature',
                          'MSSubClass','OverallCond','YrSold','MoSold'],'NA'),
                         (['Functional'],'Typ'), # Typical Functionality
                         (['KitchenQual'],'TA'),
                         (['LotFrontage'],'median'),
                         (['MSZoning'],'mode'),
                         (['SaleType','Exterior1st','Exterior2nd','SaleType'],'Oth'), #other
                         (['Electrical'],'SBrkr')]  # Standard Circuit Breakers & Romex

        #drop
        self.data = self._preprocessor.drop(self.data, drop_strategies)
        
        #fill nulls
        self.data = self._preprocessor.fillna(self.ntrain, fill_strategies)
        
        #feature engineering
        self.data = self._preprocessor.feature_engineering()
        
        #label encoder
        self.data = self._preprocessor.label_encoder(cat_cols)
        
        #normalizing
#         self.data = self._preprocessor.norm_data(self.data, num_cols)
        
        #get dummies
        self.data = self._preprocessor.get_dummies(cat_cols)
        return self.data
        