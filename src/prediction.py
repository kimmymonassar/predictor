import os
from imageai.Prediction import ImagePrediction

def runPrediction(image):
  prediction = ImagePrediction()
  prediction.setModelTypeAsResNet()
  prediction.setModelPath("./src/model/resnet50_weights_tf_dim_ordering_tf_kernels.h5")
  prediction.loadModel()
  return prediction.predictImage(image, result_count=5)