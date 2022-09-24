from deepclassifier.config import ConfigurationManager
from deepclassifier.components import DataIngestion
from deepclassifier import logger

STAGE_NAME = "01_Data_Ingestion_stage"


def main():
    try:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()
    
    except Exception as e:
        raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>{STAGE_NAME} stared<<<<<<<<<<<<<<<")
        main()
        
    except Exception as e:
        logger.exception(e)
        raise e
