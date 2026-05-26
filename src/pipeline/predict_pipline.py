import os
from pyexpat import model
import sys
from src.components.data_transformation import DataTransformationConfig
from src.logger import logging
from src.custom_exception import CustomException

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self, features):
        try:
            preprocessor_path = DataTransformationConfig().preprocessor_obj_file_path
            preprocessor = load_object(preprocessor_path)
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            logging.error(f"Error in prediction pipeline: {str(e)}")
            raise CustomException(e, sys.exc_info())