import os 
import sys 
from flask import request
from src.logger import logging
from src.constant import *
from src.exception import CustomException
from src.utils import MainUtils
from dataclasses import dataclass

@dataclass
class PredictionConfig:
     model_path=os.path.join(artifacts,MODEL)
     preprocessor_path=os.path.join(artifacts,'preprocessor.pkl')



class Prediction:
     def __init__(self):
          self.predictionconfig=PredictionConfig()
          self.utils=MainUtils()


     def load_model(self,model_path,preprocessor_path):
          try:
               logging.info("Enter into the Load Model of Prediction file ")
               model=self.utils.load_object(file_path=model_path)
               preprocessor=self.utils.load_object(file_path=preprocessor_path)
               logging.info("Successfully load the model ")
               return model ,preprocessor
          except Exception as e:
               logging.info(f"Error is {e}")
               raise CustomException(e,sys) from e
          

     def Prediction(self,model,preprocessor):
          try:
               logging.info("Enetred into the Prediction function of the Prediction file ")
               Cement =float(request.form.get('Cement'))
               Blast=float(request.form.get('Blast_Furnace_Slag'))
               Ash=float(request.form.get('Fly_Ash'))
               water=float(request.form.get('Water'))
               Superplasticizer=float(request.form.get('Superplasticizer'))
               Coarse_Aggregate=float(request.form.get('Coarse_Aggregate'))
               Fine_Aggregate=float(request.form.get('Fine_Aggregate'))
               Age=int(request.form.get('Age'))
               
               new_data=preprocessor.fit_transform([[Cement,Blast,Ash,water,Superplasticizer,Coarse_Aggregate,Fine_Aggregate,Age]])
               prediction=model.predict(new_data)
               logging.info(f"Prediction is complete and prediction is {prediction} ")
               return prediction
          except Exception as e:
               logging.info(f"Error is {e}")
               raise CustomException(e,sys) from e 
          
     def run_pipeline(self):
          try:
               logging.info('Enter into run pipeline')
               model,preprocessor=self.load_model(self.predictionconfig.model_path,self.predictionconfig.preprocessor_path)
               result=self.Prediction(model,preprocessor)
               logging.info("Congrats All are fine ")
               return result[0]
          except Exception as e:
               logging.info(f'Error is {e}')
               raise CustomException(e,sys) from e








          

