from kafka import KafkaConsumer

#! pull from YAML config
bootstrap_servers = 'localhost:9092'
kafka_topic = 'pyTest'

# Create Kafka consumer instance
consumer = KafkaConsumer(kafka_topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')

try:
    # Subscribe to the topic
    consumer.subscribe(['pyTest'])

    # Continuously listen for messages
    for message in consumer:
        print(f"Received message: {message.value.decode('utf-8')}")

except KeyboardInterrupt:
    # Close the Kafka consumer on KeyboardInterrupt
    consumer.close()
