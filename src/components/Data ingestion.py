import os
import sys
import pandas as pd
import dataclasses as dataclass
#from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split

class Dataingestconfig():
      Raw_data_path=os.path.join("artifacts","Raw_data.csv")
      Train_data_path=os.path.join("artifacts","Train_data.csv")
      Test_data_path=os.path.join("artifacts","Test_data.csv")


class data_ingestion:
      
      def __init__(self):
            self.ingestion_config=Dataingestconfig()
      
      def ingestion_data(self):
       try:
            df=pd.read_csv(os.path.join("notebook/cleaned_GemData.csv"))
            os.makedir(os.path.dirname( self.ingestion_config.Raw_data_path),exist_ok=True)
            df.to_csv( self.ingestion_config.Raw_data_path)

            train_data,test_data=train_test_split(df,test_size=0.25,random_state=42,)
            train_data.to_csv(self.ingestion_config.Train_data_path,index=False,Header=True)
            test_data.to_csv(self.ingestion_config.Test_data_path,index=False,Header=True)

            return (
                  self.ingestion_config.Train_data_path,
                  self.ingestion_config.Test_data_path
            )

       except Exception as e:
                  raise e
