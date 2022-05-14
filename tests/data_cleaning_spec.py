# data_cleaning_spec

from mamba import description, it
from expects import expect, equal

from src.carsengage2022.preprocessing.data_cleaning import Pre_processing

with description('Data Cleaning') as self:
  with it('This function is used to drop a column or row from the dataset'):
      data = {'column1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              'column2': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             }
      drop_strategies = (('column1', 0), ('column2', 1))
      expect(Pre_processing.drop(data, drop_strategies)).to(equal(data))
