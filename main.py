import json
import os
from datetime import datetime
from kafka import KafkaConsumer
from pymongo import MongoClient

MONGO_CS = os.environ.get("MONGO_CS")
MONGO_DB = os.environ.get("MONGO_DB")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION")
MONGO_CLIENT = MongoClient(MONGO_CS)
DB = MONGO_CLIENT[MONGO_DB]
EVENTS = DB[MONGO_COLLECTION]

BOOTSTRAP_SERVERS = os.environ.get("BOOTSTRAP_SERVER")
KAFKA_TOPIC = os.environ.get("TOPIC")
KAFKA_GROUP_ID = os.environ.get("KAFKA_GROUP_ID")

def main():

    auto_offset_reset = 'earliest'
    if EVENTS.find_one({}):
        auto_offset_reset = 'latest'

    try:
        consumer = KafkaConsumer(
            KAFKA_TOPIC, 
            group_id=KAFKA_GROUP_ID,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            auto_offset_reset=auto_offset_reset,
            enable_auto_commit= False) 
        
        consumer.subscribe([KAFKA_TOPIC])
        print(f"subscribed to {KAFKA_TOPIC}")

        for message in consumer:
            try:
                json_str = message.value.decode('utf-8')
                new_event = json.loads(json_str)
            except Exception:
                continue

            new_event["timestamp"] = datetime.strptime(new_event["timestamp"] ,"%Y-%m-%d %H:%M:%S")

            EVENTS.insert_one(new_event)
            print(new_event)
            consumer.commit()

    except Exception:
        consumer.close()

if __name__ == '__main__':
    main()