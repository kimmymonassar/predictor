from imageai.Prediction import ImagePrediction
import os
from keras import backend as K

def runPrediction(image, extention):
  K.clear_session()
  prediction = ImagePrediction()
  prediction.setModelTypeAsResNet()
  prediction.setModelPath("./src/model/resnet50_weights_tf_dim_ordering_tf_kernels.h5")
  prediction.loadModel()
  result = prediction.predictImage(image, result_count=5)

  #remove file
  if os.path.isfile("./images/imgToGuess." + extention):
    os.remove("./images/imgToGuess." + extention)

  return result