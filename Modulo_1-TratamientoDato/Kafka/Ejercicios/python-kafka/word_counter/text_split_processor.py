from confluent_kafka import Producer, Consumer, KafkaException

# 2 - Recibe texto aleatorio, lo parte en palabras y lo transmite
try:
    words_producer = Producer({ 'bootstrap.servers': 'localhost:9092' })
    text_consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'group1',
        'auto.offset.reset': 'earliest'
    })
    text_consumer.subscribe(['random-text'])
    words_producer.poll(0)

    while True:
        msg = text_consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print('Received text: {}'.format(msg.value().decode('utf-8')))
        words = msg.value().decode('utf-8').split()
        for word in words:
            words_producer.produce('text-split', value=word.encode('utf-8'))

except KafkaException as error:
    print(error)