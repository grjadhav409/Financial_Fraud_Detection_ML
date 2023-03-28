import pymongo
from scripts.constant.database import DATABASE_NAME
from scripts.exception import SensorException
from scripts.logger import logging
# from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
import os,sys
ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                mongo_db_url = os.getenv("MONGO_DB_URL")
                print("mongo db url:", mongo_db_url)

                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url) 
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            
        except Exception as e:
            logging.error(SensorException(e,sys))
            raise SensorException(e,sys)

