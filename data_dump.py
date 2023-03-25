import pymongo
import pandas as pd
import json
import os
import certifi
import os
ca = certifi.where()



FEATURE_FILE_PATH="/Users/ganeshjadhav/Desktop/ML_Projects/IndustryReadyFinal/CreditCardData.csv"
DATABASE_NAME="FraudDetection"
FOLDER_NAME= "CreditCardsData"
MONGO_DB_URL= "mongodb+srv://grjadhav409:Pass123@cluster1.pqs60vi.mongodb.net/?retryWrites=true&w=majority"

mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
print(mongo_client)

if __name__=="__main__":

    df_features = pd.read_csv(FEATURE_FILE_PATH)

    print(f"Rows and columns: {df_features.shape}")

    json_record_features = list(json.loads(df_features.T.to_json()).values())
    print(json_record_features[0])

    #insert converted json record to mongo db
    mongo_client[DATABASE_NAME][FOLDER_NAME].insert_many(json_record_features)
    print("data dumped to mongodb")


