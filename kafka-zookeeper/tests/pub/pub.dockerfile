FROM python:3.9

WORKDIR /app

COPY pub.py .

RUN pip install confluent-kafka

CMD ["python", "pub.py"]
