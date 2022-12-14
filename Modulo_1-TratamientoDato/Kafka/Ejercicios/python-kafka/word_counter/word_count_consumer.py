from confluent_kafka import Producer, Consumer, KafkaException

# 4 - Consume las cuentas de las palabras recibidas
try:
    word_counter = {}
    word_counter_consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'group1',
        'auto.offset.reset': 'earliest'
    })
    word_counter_consumer.subscribe(['word-counter'])

    while True:
        msg = word_counter_consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("word_count error: {}".format(msg.error()))
            continue

        word = msg.key().decode('utf-8')
        count = msg.value().decode('utf-8')
        word_counter[word] = count
        print(f" {word} => {count}")

except KafkaException as error:
    print(error)
