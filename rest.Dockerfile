FROM python:3.8.2
RUN mkdir /project/
WORKDIR /project/
RUN git clone https://github.com/Arnacels/testfastapi.git .
RUN git pull origin master
RUN pip install -r requirements.txt
WORKDIR /project/consumer
RUN python3 consumer.py
WORKDIR /project/testrest
RUN uvicorn main:app --reload