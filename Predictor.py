from imageai.Prediction import ImagePrediction
import os
import json
from flask import Flask
from flask_restful import Api, Resource
from PIL import Image
import requests
from io import BytesIO
from flask import request
import numpy as np

app = Flask(__name__)
api = Api(app)

class Predictor(Resource):
  def get(self):
    return 'running', 200

  def post(self):
    imgUrl = request.args.get('imgUrl')
    response = requests.get(imgUrl)
    imgFile = Image.open(BytesIO(response.content))
    currentDir = os.getcwd()
    imgFile.save(currentDir  + '/images/' + 'imgToGuess.' + imgFile.format)

    predictions, percentage_probabilities = runPrediction(currentDir  + '/images/' + 'imgToGuess.' + imgFile.format)

    data = []

    for index in range(len(predictions)):
      item = {
        predictions[index] : percentage_probabilities[index]
      }
      json.dumps(data)
      data.append(item)
    
    return data

def runPrediction(image):
  prediction = ImagePrediction()
  prediction.setModelTypeAsResNet()
  prediction.setModelPath("./model/resnet50_weights_tf_dim_ordering_tf_kernels.h5")
  prediction.loadModel()
  return prediction.predictImage(image, result_count=5)

api.add_resource(Predictor, "/")
app.run(debug=True)
