
from datetime import datetime
import os
from sensor.constant  import training_pipeline

class TrainingPipelineConfig:

    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name: str = training_pipeline.PIPELINE_NAME
        self.artifact_dir: str = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)
        self.timestamp: str = timestamp