FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

# RUN chmod 777 ./wait-for-it.sh wait-for-it.sh

# CMD python app.py
