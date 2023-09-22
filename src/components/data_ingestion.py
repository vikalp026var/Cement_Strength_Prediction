import os 
import sys 
from src.logger import logging
from src.exception import CustomException
from src.constant import * 
from src.utils import MainUtils
import pymongo
import pandas as pd
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    data=os.path.join(dataset)
    artifacts=os.path.join(artifacts)


class DataIngestion:
    def __init__(self) :
        self.data_ingestionconfig=DataIngestionConfig()
        self.utils=MainUtils()
    

    def Collection(self):
        try:
            logging.info("Entered into the data Ingestion of Data Ingestion")
            client=pymongo.MongoClient(MONGODB_URL)
            df=client[MONGODB_DB_NAME]
            collection=df[MONDODB_COLLECTION_NAME]
            logging.info("Exited from the DataIngestion Colllection")
            return collection
        except Exception as e:
            raise CustomException(e,sys) from e
        

    def DataFrame(self):
        try:
            logging.info('Entered into The Dataframe of Data Ingestion ')
            collection=self.Collection()
            data=collection.find({})
            df=pd.DataFrame(data)
            df.drop(columns=['_id'],axis=1,inplace=True)
            logging.info("Exited from the Data Frame of Data Ingestion")
            return df 
        except Exception as e:
            raise CustomException(e,sys) from e
        


    def file_save(self):
        try:
            logging.info('Entered into the file save of Data Ingestion')
            df=self.DataFrame()
            os.makedirs(self.data_ingestionconfig.artifacts,exist_ok=True)
            logging.info("Successfully make the artifact folder")
            raw_file_path=os.path.join(self.data_ingestionconfig.artifacts,self.data_ingestionconfig.data)
            df.to_csv(raw_file_path,index=False)
            logging.info("Successfully make the csv file and save the artifacts ")
            return raw_file_path
        except Exception as e:
            raise CustomException(e,sys) from e
        

    def data_ingestion(self):
        try:
            logging.info('!!! Entered into The Data Ingestion file ')
            file_path=self.file_save()
            return file_path
        except Exception as e:
            raise CustomException(e,sys) from e

        
    

            
          