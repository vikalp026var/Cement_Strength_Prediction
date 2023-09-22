import os 
import sys 
import pickle 
from logger import logging
from exception import CustomException
from constant import *

class MainUtilsConfig:
    artifact=os.path.join(artifacts)

class MainUtils:
    def __init__(self):
        self.mainutilsconfig=MainUtilsConfig()


    @staticmethod
    def save_object(self,file_path,object):
        try:
            logging.info("Entered into save object of MainUtil ")
            with open(file_path,'wb') as obj:
                pickle.dump(object,obj)
            logging.info('Model pickle is save successfully')
        except Exception as e:
            raise CustomException(e,sys) from e
        

    @staticmethod
    def load_object(self,file_path):
        try:
            logging.info("Entered into the load object of MainUtils ")
            with open(file_path,'rb') as f:
                model=pickle.load(f)
            logging.info("Exited from the load object suuccessfully ")
            return model
        except Exception as e:
            raise CustomException(e,sys) from e 
        

          
                