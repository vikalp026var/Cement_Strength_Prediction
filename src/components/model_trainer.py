import os 
import sys 
from src.constant import * 
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from src.utils import MainUtils
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


@dataclass
class ModelTrainConfig:
    models={
     'LinearRegression':LinearRegression(),
     'RandomForest':RandomForestRegressor(),
    'Lasso':Lasso(),
    'Ridge':Ridge(),
    'ElasticNet':ElasticNet(),
    'DecisionTreeRegressor':DecisionTreeRegressor(),
   ' KNeighborsRegressor':KNeighborsRegressor()
    }
    model_path=os.path.join(artifacts,MODEL)
class ModelTrainer:
    def __init__(self):
        self.ModelTrainConfig=ModelTrainConfig()
        self.utils =MainUtils()
   

    def model_evalutaion(self,y_test,y_pred):
        try:
            logging.info("Entered into the model evaluation")
            score=mean_squared_error(y_test,y_pred)
            score1=r2_score(y_test,y_pred)
            logging.info("Exited from the model evaluation ")
            return score,score1
        except CustomException as e:
            raise CustomException(e,sys ) from e 
        

    


    def model_train(self, models, X_train_scale, X_test_scale, y_train, y_test):
        try:
            report = {}
            logging.info('Entered into the model train of the model train')
        
            for i, j in models.items():
                model = j
                model.fit(X_train_scale, y_train)
                y_pred = model.predict(X_test_scale)
                score, score1 = self.model_evalutaion(y_test, y_pred)
                report[i] = score1  
                logging.info(f"Model {i} evaluation metric 1: {score}")
                logging.info(f"Model {i} evaluation metric 2: {score1}")
        
            logging.info("After the loop")
        
            best_model_name, _ = max(report.items(), key=lambda x: x[1])
            best_model = models[best_model_name]
            return best_model_name, best_model
            # returning the model name and its maximum score

        except Exception as e:
            logging.info(f"Error during model training: {e}")
            raise CustomException(e,sys) from e
        

    def loaded_model(self, X_train_scale, X_test_scale, y_train, y_test):
        try:
            logging.info("Entered into the loaded model ")
            model_name, model = self.model_train(self.ModelTrainConfig.models, X_train_scale, X_test_scale, y_train, y_test)
            return model_name,model
        except CustomException as e:
            logging.info(f"Error during the loaded model ")
            raise CustomException(e, sys) from e

        


        
    def model_train_initiate(self,X_train_scale, X_test_scale, y_train, y_test):
        try:
            logging.info("ENtered into the model initae part ")
            model_name,model=self.loaded_model(X_train_scale, X_test_scale, y_train, y_test)
            return model_name,model
            logging.info("Exited from the model train initaiet part ")
        except Exception as e:
            logging.info(f"Error is Model Train part {e}")
            raise CustomException(e,sys) from e


            
                

        