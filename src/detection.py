from imageai.Detection import ObjectDetection
import os
import time
from base64 import b64encode
from keras import backend as K

ENCODING = "utf-8"

execution_path = os.getcwd()

def runDetection(image, extention):
  K.clear_session()
  detector = ObjectDetection()
  detector.setModelTypeAsRetinaNet()
  detector.setModelPath("./src/model/resnet50_coco_best_v2.0.1.h5")
  detector.loadModel()
  detector.detectObjectsFromImage(input_image=image, output_image_path="./images/imgToGuessNew." + extention, minimum_percentage_probability=30)
  
  while not os.path.exists("./images/imgToGuessNew." + extention):
    time.sleep(1)

  if os.path.isfile("./images/imgToGuessNew." + extention):
    with open("./images/imgToGuessNew." + extention, "rb") as img_file:
      byte_content = img_file.read()
  
  #remove files
  os.remove("./images/imgToGuessNew." + extention)
  if os.path.isfile("./images/imgToGuess." + extention):
    os.remove("./images/imgToGuess." + extention)
  
  base64_bytes = b64encode(byte_content)
  base64_string = base64_bytes.decode(ENCODING)
  raw_data = {'base64': base64_string}
  return raw_data