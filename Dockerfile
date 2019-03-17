FROM python:3.6-slim

COPY . /app
WORKDIR /app

ADD https://www.dropbox.com/s/v0yglzh6ac7y58u/resnet50_weights_tf_dim_ordering_tf_kernels.h5?dl=0 ./model/resnet50_weights_tf_dim_ordering_tf_kernels.h5
ADD https://www.dropbox.com/s/70joz3q5zuw27ii/resnet50_coco_best_v2.0.1.h5?dl=0 ./model/resnet50_coco_best_v2.0.1.h5

RUN apt-get update && apt-get install libsm6 libxrender1 libfontconfig1 libglib2.0
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./src/main.py" ]