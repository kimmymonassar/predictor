FROM python:3.6-alpine

COPY . /app
WORKDIR /app

RUN pip install setuptools
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "./Predictor.py" ]