from faker import Faker
from confluent_kafka import Producer, KafkaException

# 1 - Transmite texto aleatorio
try:
    faker = Faker()
    text_producer = Producer({'bootstrap.servers': 'localhost:9092'})

    for i in range(10):
        msg = faker.text()
        text_producer.produce('random-text', msg.encode('utf-8'))
        text_producer.flush()
except KafkaException as error:
    print(error)



