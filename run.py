"""
Main script to run the data injection pipeline
"""
import sys
from src.logger import logging
from src.custom_exception import CustomException
from src.components.data_injestion import DataInjestion


def main():
    try:
        logging.info("Starting data injection process...")
        
        # Initialize and run data injection
        data_injestion = DataInjestion()
        train_path, test_path = data_injestion.initiate_data_injestion()
        
        logging.info(f"✓ Data injection completed successfully!")
        logging.info(f"  Train data saved to: {train_path}")
        logging.info(f"  Test data saved to: {test_path}")
        
        print("\n" + "="*50)
        print("DATA INJECTION COMPLETED SUCCESSFULLY!")
        print("="*50)
        print(f"Train data: {train_path}")
        print(f"Test data: {test_path}")
        print("="*50 + "\n")
        
        return train_path, test_path
        
    except Exception as e:
        logging.error(f"Error during data injection: {str(e)}")
        raise CustomException(e, sys)


if __name__ == "__main__":
    main()
