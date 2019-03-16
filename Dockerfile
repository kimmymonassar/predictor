FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN ls
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./Predictor.py" ]