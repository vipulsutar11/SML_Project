import numpy as np
import pandas as pd
import os 
from src.logger import logging
from src.custom_exception import CustomException
import sys
from dataclasses import dataclass

@dataclass
class DataInjestionConfig():
    raw_data_path: str = os.path.join('artifacts', 'StudentsPerformance.csv')
    train_data_path: str = os.path.join('artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('artifacts', 'test_data.csv')

class DataInjestion:
    def __init__(self):
        self.data_injestion_config = DataInjestionConfig()

    def initiate_data_injestion(self):
        logging.info("Data Injestion method starts")
        try:
            raw_path = self.data_injestion_config.raw_data_path
            if not os.path.exists(raw_path):
                raw_path = os.path.join('notebook', 'data', 'stud.csv')

            df = pd.read_csv(raw_path)
            logging.info(f"Dataset read as pandas dataframe from {raw_path}")

            os.makedirs(os.path.dirname(self.data_injestion_config.train_data_path), exist_ok=True)

            from sklearn.model_selection import train_test_split

            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

            train_df.to_csv(self.data_injestion_config.train_data_path, index=False, header=True)
            test_df.to_csv(self.data_injestion_config.test_data_path, index=False, header=True)
            logging.info("split the data into train and test data")

            return (self.data_injestion_config.train_data_path, self.data_injestion_config.test_data_path)

        except Exception as e:
            logging.info("Exception occurred in data injestion method")
            raise CustomException(e, sys)