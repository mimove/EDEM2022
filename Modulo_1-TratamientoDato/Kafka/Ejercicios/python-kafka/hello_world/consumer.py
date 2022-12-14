from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'group1',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['myTopicTest'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    # print(f" key: {msg.key().decode('utf-8')}; value: {msg.value().decode('utf-8')}")
    print(f" key: {msg.key()}; value: {msg.value()}")

c.close()
