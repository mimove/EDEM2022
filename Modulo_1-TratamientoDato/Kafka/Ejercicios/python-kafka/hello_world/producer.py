from confluent_kafka import Producer

producer = Producer({
        'bootstrap.servers': 'localhost:9092'
        })

producer.poll(0)
for i in range(6):
    msg = f" python {i}"
    # producer.produce('myTopic', value=msg.encode('utf-8'), key=f'{i}:'.encode('utf-8'))
    producer.produce('myTopicTest', value=msg, key=f'{i}:')
    producer.flush()


