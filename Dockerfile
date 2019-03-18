FROM python:3.6-slim

COPY . /app
WORKDIR /app

ADD https://www.dropbox.com/s/v0yglzh6ac7y58u/resnet50_weights_tf_dim_ordering_tf_kernels.h5?dl=1 ./src/model/resnet50_weights_tf_dim_ordering_tf_kernels.h5
ADD https://www.dropbox.com/s/70joz3q5zuw27ii/resnet50_coco_best_v2.0.1.h5?dl=1 ./src/model/resnet50_coco_best_v2.0.1.h5

RUN apt-get update -y && apt-get install -y \
    libsm6 \ 
    libxrender1 \ 
    libfontconfig1 \ 
    libglib2.0 \ 
    libxext-dev \ 
    libxtst-dev \
    build-essential \
    cmake \
    git \
    libgtk2.0-dev \
    pkg-config \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev

RUN apt-get update && apt-get -y install libglib2.0; apt-get clean
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./src/main.py" ]