from imageai.Detection import ObjectDetection
import os
from base64 import b64encode

ENCODING = "utf-8"

execution_path = os.getcwd()

def runDetection(image, extention):
  detector = ObjectDetection()
  detector.setModelTypeAsRetinaNet()
  detector.setModelPath("./src/model/resnet50_coco_best_v2.0.1.h5")
  detector.loadModel()
  detector.detectObjectsFromImage(input_image=image, output_image_path="./images/imgToGuessNew." + extention, minimum_percentage_probability=30)
  with open("./images/imgToGuessNew." + extention, "rb") as img_file:
    byte_content = img_file.read()
  
  #remove file
  os.remove("./images/imgToGuessNew." + extention)
  os.remove("./images/imgToGuess." + extention)
  
  base64_bytes = b64encode(byte_content)
  base64_string = base64_bytes.decode(ENCODING)
  raw_data = {'base64': base64_string}
  return raw_data