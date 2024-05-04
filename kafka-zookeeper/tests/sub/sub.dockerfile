FROM python:3.9

WORKDIR /app

COPY sub.py .

RUN pip install confluent-kafka

CMD ["python", "sub.py"]
