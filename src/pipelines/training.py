import os 
import sys 
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV
from src.utils import MainUtils
from src.constant import *
from sklearn.metrics import r2_score
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from dataclasses import dataclass


@dataclass
class TrainingConfig:
    param_grid = { 
    'n_estimators': [300],
    'max_features': [ 'sqrt'],
    'max_depth' : [4,5,6,7,9,10,11,12,14,15],
    'criterion' :['squared_error']
    }
    model_path=os.path.join(artifacts,MODEL)


class Training_Pipeline:
    def __init__(self):
        self.Training_config=TrainingConfig()
        self.utils=MainUtils()
        self.data_ingestion=DataIngestion()
        self.data_transform=DataTransformation()
        self.model_train=ModelTrainer()
     
        
    def Hypertuning(self,model_name,model,X_train,X_test,y_train,y_test):
        try:
            logging.info("Entered into the Hypertuning of Training ")
            clf=GridSearchCV(model,param_grid=self.Training_config.param_grid,cv=5,verbose=2)
            clf.fit(X_train,y_train)
            y_pred_tune=clf.predict(X_test)
            clf.best_params_
            score_hyper=r2_score(y_test,y_pred_tune)
            self.utils.save_object(self.Training_config.model_path, clf)
            logging.info(f"Successfully Hypertunned and saved the model to the hard disk as a pickle file. The best model is {model_name} and score is  {score_hyper}.")
        except Exception as e:
            logging.info(f'Error during the hypertuning of the model ')
            raise CustomException(e,sys) from e


    def Training_pipeline_initiate(self):
        try:
            logging.info("Entered into the Training pipeline initiate")
            file_path=self.data_ingestion.data_ingestion()
            X_train_scale,X_test_scale,y_train,y_test=self.data_transform.Data_Transformation_Intiate(file_path)
            model_name,model=self.model_train.model_train_initiate(X_train_scale,X_test_scale,y_train,y_test)
            self.Hypertuning(model_name,model,X_train_scale,X_test_scale,y_train,y_test)
            logging.info("Successfully Training ")
        except Exception as e:
            logging.info(f"Error during training is {e}")
            raise CustomException(e,sys ) from e
        



    





