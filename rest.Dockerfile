FROM python:3.8.2
RUN mkdir /project/
WORKDIR /project/
RUN git clone https://github.com/Arnacels/testfastapi.git .
RUN git pull origin master
RUN pip install -r requirements.txt
WORKDIR /project/testrest