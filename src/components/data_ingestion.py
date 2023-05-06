"""
Here all the data ingestion tasks will be performed
"""

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # Used to create class variables

# Any input that is required for data ingestion will be provided by this class
@dataclass
class DataIngestionConfig:
    # dataclass is used to define class variables
    # Input to data ingestion component
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config=DataIngestionConfig()
    
    # Read data from data source
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component")

        # This is a general data ingestion task we can read data from anywhere (Database, api etc)
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Exported data into dataframe')

            # dirname to get root dir
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train Test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=34)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion completed")

            # The return objects will be used for data transformation
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as E:
            raise CustomException(E,sys)


if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()