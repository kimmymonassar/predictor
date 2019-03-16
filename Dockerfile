FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN ls
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "./Predictor.py" ]