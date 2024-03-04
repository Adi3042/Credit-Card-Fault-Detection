from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
import os,sys

from src.pipeline.train_pipeline import TraininingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html') 


@app.route("/train.html")
def train_route():
    try:

        train_pipeline = TraininingPipeline()
        train_pipeline.run_pipeline()

        return render_template('upload_file.html') 

    except Exception as e:
        raise CustomException(e,sys)


@app.route('/upload_file.html', methods=['POST', 'GET'])
def upload():
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                # Display a JavaScript alert to prompt the user to provide a file
                return render_template('upload_file.html')

            prediction_pipeline = PredictionPipeline(request)
            prediction_file_detail = prediction_pipeline.run_pipeline()

            lg.info("Prediction completed. Downloading prediction file.")
            return send_file(prediction_file_detail.prediction_file_path,
                             download_name=prediction_file_detail.prediction_file_name,
                             as_attachment=True)

        else:
            return render_template('upload_file.html')
    except Exception as e:
        raise CustomException(e,sys)
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug= True)