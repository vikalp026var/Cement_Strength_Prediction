import os 
import sys 
import pickle 
from src.logger import logging
from src.exception import CustomException
from src.constant import *

class MainUtilsConfig:
    artifact=os.path.join(artifacts)

class MainUtils:
    def __init__(self):
        self.mainutilsconfig=MainUtilsConfig()


    @staticmethod
    def save_object(file_path,object):
        try:
            logging.info("Entered into save object of MainUtil ")
            with open(file_path,'wb') as obj:
                pickle.dump(object,obj)
            logging.info('Model pickle is save successfully')
        except Exception as e:
            raise CustomException(e,sys) from e
        

    @staticmethod
    def load_object(file_path):
        try:
            logging.info("Entered into the load object of MainUtils ")
            with open(file_path,'rb') as f:
                model=pickle.load(f)
            logging.info("Exited from the load object suuccessfully ")
            return model
        except Exception as e:
            raise CustomException(e,sys) from e 
        

          
                