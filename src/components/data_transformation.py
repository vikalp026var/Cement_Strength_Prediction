from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from src.utils import MainUtils
import os 
import pandas as pd 
import sys
from src.constant import *
from dataclasses import dataclass


@dataclass
class DataTransformationConfig:
#     artifact=os.path.join(artifacts)
    train_path=os.path.join(artifacts,'train.csv')
    test_path=os.path.join(artifacts,'test.csv')
    preprocessor=os.path.join(artifacts,'preprocessor.pkl')
    

class DataTransformation:
    def __init__(self):
        self.dataTransformation=DataTransformationConfig()
        self.utils=MainUtils()

    def data_read(self,file_path):
        try:
            logging.info("Entered into the data read ")
            data=pd.read_csv(file_path)
            logging.info("exited from data read ")
            return data
        except Exception as e:
            logging.info(f"Exception is {e}")
            raise CustomException(e,sys) from e
        

    def split_data(self,data):
        try:
            logging.info("Entered into the split data of Data Tranformation")
            X=data.iloc[:,:-1]
            y=data.iloc[:,-1]
            logging.info("Successfully split the data ")

            return X,y
        except Exception as e:
            logging.info(f"Exception of split data  is {e}")
            raise CustomException(e,sys) from e
        


    def train_test(self, X, y):
        try:
            logging.info("Entered into the train-test method of Data Transformation")
        # Fix 1: Correct unpacking
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.23, random_state=42)
        
            X_train_data = pd.DataFrame(X_train)
            X_test_data = pd.DataFrame(X_test)
            y_train_data = pd.DataFrame(y_train)
            y_test_data = pd.DataFrame(y_test)
        
        # Fix 2: Correct DataFrame concatenation
            train_data = pd.concat([X_train_data, y_train_data], axis=1)
            test_data = pd.concat([X_test_data, y_test_data], axis=1)
            train_data.to_csv(self.dataTransformation.train_path, index=False)
            test_data.to_csv(self.dataTransformation.test_path, index=False)
        
            logging.info("Train and Test files are saved into the artifact folder")
            logging.info("Exited from the train-test method")

            return X_train, y_train, X_test, y_test
        except Exception as e:
            logging.error(f"Exception is {e}")
            raise CustomException(e, sys) from e

    def Standarad(self,X_train,X_test):
        try:
            logging.info("Entered into the Standard of Data Transformation")
            scale=StandardScaler()
            self.utils.save_object(self.dataTransformation.preprocessor,scale)
            logging.info("Successfully save the preprocessor ")
            X_train_scale=scale.fit_transform(X_train)
            X_test_scale=scale.transform(X_test)
            logging.info("Exited from the Standard Method after Scaling train and test ")
            return X_train_scale,X_test_scale
        except Exception as e:
            logging.info(f"Exception  is {e}")
            raise CustomException(e,sys) from e
        

    def Data_Transformation_Intiate(self,file_path):
        try:
            logging.info("Entered into the Data Transfomration Initaite ")
            data=self.data_read(file_path=file_path)
            X,y=self.split_data(data)
            X_train,y_train,X_test,y_test=self.train_test(X,y)
            X_train_scale,X_test_scale=self.Standarad(X_train,X_test)
            logging.info("Successfully run Data Transfomation file 1")
            return X_train_scale,X_test_scale,y_train,y_test
        except Exception as e:
            logging.info(f"Exception  is {e}")
            raise CustomException(e,sys) from e



        
    
            
        

