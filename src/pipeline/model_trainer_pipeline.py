from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src import logger

STAGE_NAME = "Model Trainer Pipeline"

class ModelTrainerPipeline:
    def __init__(self):
        pass


    def initiate_model_trainer(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_training_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()

        except Exception as e:
            raise e
