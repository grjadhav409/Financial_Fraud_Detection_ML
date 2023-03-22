from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
import sys
from sensor.pipeline.training_pipeline import TrainingPipeline
if __name__ == '__main__':
    try:

        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
    
    except Exception as e:
        print(e)
        logging.error(e)
    