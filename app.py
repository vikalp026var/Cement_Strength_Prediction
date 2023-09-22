from flask import Flask,render_template,jsonify,request,app
from src.pipelines.training import Training_Pipeline
from src.pipelines.prediction import Prediction
from src.exception import CustomException
from src.logger import logging
import sys



app=Flask(__name__)


@app.route('/')
def home():
     return "Welcome To cement Strength Prediction"

@app.route('/train')
def train():
     try:
          obj=Training_Pipeline()
          obj.Training_pipeline_initiate()
          return render_template('index.html')
     except Exception as e:
          raise CustomException (e,sys) from e
     

@app.route('/prediction',methods=['POST','GET'])
def predict():
     try:
          obj1=Prediction()
          result=obj1.run_pipeline()
          return render_template('index.html',result=result)
     except Exception as e:
          raise CustomException(e,sys) from e
     

if __name__ == '__main__':
    app.run(debug=True,port=8000)