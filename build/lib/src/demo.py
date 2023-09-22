from src.components.data_ingestion import DataIngestion
import os 
import sys 
import sys
sys.path.insert(0, "C:/Users/PC/Desktop/Cement_Strength_Prediction")
obj=DataIngestion()
file=obj.data_ingestion()
print(file)