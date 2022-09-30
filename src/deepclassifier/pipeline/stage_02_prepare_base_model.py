from deepclassifier.config import ConfigurationManager
from deepclassifier.components import PrepareBaseModel
from deepclassifier import logger

STAGE_NAME = "prepare base model"

def main():
    config = configurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()

if __name__ == "__main__":
    try:
        logger.info(f"***********************************")
        logger.info(f">>>>>>>>>>>>>>>>stage 02 {STAGE_NAME} has started<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        main()
        logger.info(f">>>>>>>>>>>>>>>>stage 02 {STAGE_NAME} complete<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e