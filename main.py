from kafka import KafkaConsumer

def main():
    #! enviroment variables change
    bootstrap_servers = 'localhost:9092'
    kafka_topic = 'pyTest'

    consumer = KafkaConsumer(kafka_topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')

    try:
        consumer.subscribe(['pyTest'])

        for message in consumer:
            print(f"Received message: {message.value.decode('utf-8')}")

    except KeyboardInterrupt:
        consumer.close()

if __name__ == '__main__':
    main()