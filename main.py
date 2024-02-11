import json
import os
from datetime import datetime
from kafka import KafkaConsumer
from pymongo import MongoClient 


MONGO_CS = os.environ.get("MONGO_CS") #'mongodb://admin:admin@localhost:27017' 
MONGO_CLIENT = MongoClient(MONGO_CS)
DB = MONGO_CLIENT.testdb

def main():
    
    bootstrap_servers = os.environ.get("BOOTSTRAP_SERVER")
    kafka_topic = os.environ.get("TOPIC")

    events = DB.events
    most_recent_doc = events.find_one({}, sort=[("timestamp", -1)])
    print(most_recent_doc)

    try:
        consumer = KafkaConsumer(kafka_topic, bootstrap_servers=bootstrap_servers,
                             auto_offset_reset='earliest') 
        consumer.subscribe([kafka_topic])
        print(f"subscribed to {kafka_topic}")

        for message in consumer:
            json_str = message.value.decode('utf-8')
            new_event = json.loads(json_str)
            new_event["timestamp"] = datetime.strptime(new_event["timestamp"] ,"%Y-%m-%d %H:%M:%S")

            if most_recent_doc is None or new_event["timestamp"] > most_recent_doc["timestamp"]:
                events.insert_one(new_event)
                most_recent_doc = new_event
                print(new_event)

    except Exception:
        consumer.close()

if __name__ == '__main__':
    main()