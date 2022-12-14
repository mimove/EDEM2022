from confluent_kafka import Producer, Consumer, KafkaException

# 3 - Cuenta las palabras receibidas y las transmite
try:
    word_counter = {}
    word_counter_producer = Producer({ 'bootstrap.servers': 'localhost:9092' })
    word_consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'group1',
        'auto.offset.reset': 'earliest'
    })
    word_consumer.subscribe(['text-split'])

    while True:
        msg = word_consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("word_count error: {}".format(msg.error()))
            continue
        word = msg.value().decode('utf-8')
        word_counter[word] = word_counter.get(word, 0) + 1
        print(f'Received word: {word}, count: {word_counter[word]}')
        word_counter_producer.produce('word-counter',
                                      key=word.encode('utf-8'), value=str(word_counter[word]).encode('utf-8'))

except KafkaException as error:
    print(error)
