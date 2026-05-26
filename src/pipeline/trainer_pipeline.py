"""
Training Pipeline - orchestrates the end-to-end ML pipeline
"""
from src.components.data_injestion import DataInjestion
from src.logger import logging
from src.custom_exception import CustomException
import sys


class TrainerPipeline:
    def __init__(self):
        self.data_injestion = DataInjestion()
    
    def initiate_trainer_pipeline(self):
        try:
            logging.info("Starting trainer pipeline...")
            
            # Step 1: Data Injection
            logging.info("Step 1: Initiating data injection...")
            train_data_path, test_data_path = self.data_injestion.initiate_data_injestion()
            logging.info(f"Data injection completed. Train: {train_data_path}, Test: {test_data_path}")
            
            # TODO: Step 2: Data Transformation
            # from src.components.data_transformation import DataTransformation
            # logging.info("Step 2: Data transformation in progress...")
            
            # TODO: Step 3: Model Training
            # from src.components.model_trainer import ModelTrainer
            # logging.info("Step 3: Model training in progress...")
            
            logging.info("Training pipeline completed successfully!")
            return train_data_path, test_data_path
            
        except Exception as e:
            logging.error(f"Error in training pipeline: {str(e)}")
            raise CustomException(e, sys)


if __name__ == "__main__":
    pipeline = TrainerPipeline()
    pipeline.initiate_trainer_pipeline()
