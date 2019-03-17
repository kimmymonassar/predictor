import os
import json
from prediction import runPrediction
from detection import runDetection
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from PIL import Image
import requests
from io import BytesIO
from flask import request
import numpy as np

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class Detector(Resource):
  def get(self):
    return 'running', 200

  def post(self):
    # try:
    imgUrl = request.args.get('imgUrl')
    response = requests.get(imgUrl)
    imgFile = Image.open(BytesIO(response.content))
    currentDir = os.getcwd()
    
    if imgFile.format.lower().endswith(('png', 'jpg', 'jpeg')):
      imgFile.save(currentDir  + '/images/' + 'imgToGuess.' + imgFile.format)

      detectionBase64 = runDetection(image=currentDir  + '/images/' + 'imgToGuess.' + imgFile.format, extention=imgFile.format)
      
      data = []
      data.append(json.dumps(detectionBase64))
      
      return data, 200
    else:
      return 'Unsupported file format, valid format is PNG, JPG, JPEG', 500
    # except:
    #   return 'Something went wrong', 500

class Predictor(Resource):
  def get(self):
    return 'running', 200

  def post(self):
    try:
      imgUrl = request.args.get('imgUrl')
      response = requests.get(imgUrl)
      imgFile = Image.open(BytesIO(response.content))
      currentDir = os.getcwd()

      if imgFile.format.lower().endswith(('png', 'jpg', 'jpeg')):
        imgFile.save(currentDir  + '/images/' + 'imgToGuess.' + imgFile.format)

        predictions, percentage_probabilities = runPrediction(image=currentDir  + '/images/' + 'imgToGuess.' + imgFile.format, extention=imgFile.format)

        data = []

        for index in range(len(predictions)):
          item = {
            predictions[index] : percentage_probabilities[index]
          }
          json.dumps(data)
          data.append(item)
        
        return data, 200
      else:
        return 'Unsupported file format, valid format is PNG, JPG, JPEG', 500
    except:
      return 'Something went wrong', 500

port = int(os.environ.get('PORT', 5000))
api.add_resource(Predictor, "/predict")
api.add_resource(Detector, "/detect")
app.run(debug=True, host='0.0.0.0', port=port)