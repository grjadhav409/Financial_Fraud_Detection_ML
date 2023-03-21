from sensor.entity.config_entity import TrainingPipelineConfig
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataInjestionArtifact
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.components.data_injestion import DataInjestion
import os
import sys

class TrainingPipeline():

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()


    def start_data_ingestion(self)->DataInjestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            data_ingestion = DataInjestion(data_injestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_injestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except  Exception as e:
            raise  SensorException(e,sys)

        
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            logging.error(SensorException(e,sys))
            raise SensorException(e,sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            logging.error(SensorException(e,sys))
            raise SensorException(e,sys)
        
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            logging.error(SensorException(e,sys))
            raise SensorException(e,sys)
        
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.error(SensorException(e,sys))
            raise SensorException(e,sys)
        
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            logging.error(SensorException(e,sys))
            raise SensorException(e,sys)
        

    def run_pipeline(self):
        try:
            data_injestion_artifact: DataInjestionArtifact = self.start_data_ingestion()
        except Exception as e:
            logging.error(SensorException(e,sys))
            raise SensorException(e,sys)