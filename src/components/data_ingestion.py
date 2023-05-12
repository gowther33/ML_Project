"""
Here all the data ingestion tasks will be performed
"""

import os
import sys
from dataclasses import dataclass # Used to create class variables

from sklearn.model_selection import train_test_split
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import Data_TransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


# Any input that is required for data ingestion will be provided by this class
@dataclass
class DataIngestionConfig:
    # dataclass is used to define class variables
    # Input to data ingestion component
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
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
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as E:
            raise CustomException(E,sys)


if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_tranformation = DataTransformation()
    train_arr, test_arr, _ = data_tranformation.initiate_data_transformation(train_data, test_data)

    # Here we will call model trainer and get best r2_score
    model_trainer = ModelTrainer()
    score = model_trainer.initiate_model_trainer(train_arr, test_arr)

    print(f"r2_score:{score}")