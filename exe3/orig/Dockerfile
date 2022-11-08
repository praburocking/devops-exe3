
#FROM jwilder/dockerize
FROM python:3.9
WORKDIR /usr/src/orig
COPY . .
RUN pip install pika
CMD ["python3", "orig.py"]
#CMD dockerize -wait tcp://exe3-rabitmq-1:5672 -timeout 30s python3 orig.py 
