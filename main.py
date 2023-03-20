from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
import sys

# for testing exceptions
def test_exceptions():
    try:
        logging.info("Test exception of division")
        x= 1/0
    except Exception as e:
        
        raise SensorException(e,sys)


if __name__ == '__main__':
    # # test-1:
    # mongo_client = MongoDBClient()

    # print(mongo_client.database.list_collection_names())

    # # test-2:
    try:
        test_exceptions()

    except Exception as e:
        logging.error(e)
        raise Exception