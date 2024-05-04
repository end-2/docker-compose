import time
import logging
from confluent_kafka import Consumer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup', 'auto.offset.reset': 'earliest'})
c.subscribe(['dummy'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        logger.info('Consumer error: {}'.format(msg.error()))
        continue

    logger.info('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()
