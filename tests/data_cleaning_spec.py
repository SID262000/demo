# data_cleaning_spec

from mamba import it, description
from expects import expect, equal

from src.carsengage2022.preprocessing.data_cleaning import Pre_processing

with description('Data Cleaning') as self:
    with it('should count the total missing values in the dataset'):
        df = Pre_processing().drop()
        expect(df.isnull().sum()[0]).to(equal(0))

    with it('drop a column'):
      expect(Pre_processing().drop().iloc[0][0]).to(equal('Tata'))
    
    with it('fill missing values'):
      expect(Pre_processing().fill_missing_values().iloc[0][1]).to(equal('Nano Genx'))