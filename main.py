import json
from datetime import datetime
from kafka import KafkaConsumer
from pymongo import MongoClient
from config import BOOTSTRAP_SERVER , TOPIC , KAFKA_GROUP_ID , MONGO_CS , MONGO_DB , MONGO_COLLECTION , ENCODING , DATETIME_FORMAT 


MONGO_CLIENT = MongoClient(MONGO_CS)
DB = MONGO_CLIENT[MONGO_DB]
EVENTS = DB[MONGO_COLLECTION]

def main():
    auto_offset_reset = 'earliest'
    if EVENTS.find_one({}):
        auto_offset_reset = 'latest'

    try:
        consumer = KafkaConsumer(
            TOPIC, 
            group_id=str(KAFKA_GROUP_ID),
            bootstrap_servers=BOOTSTRAP_SERVER,
            auto_offset_reset=auto_offset_reset,
            enable_auto_commit= False) 
        
        consumer.subscribe([TOPIC])
        print(f"subscribed to {TOPIC}")

        for message in consumer:
            try:
                json_str = message.value.decode(ENCODING)
                new_event = json.loads(json_str)
            except Exception:
                consumer.commit()
                continue

            new_event["timestamp"] = datetime.strptime(new_event["timestamp"] ,DATETIME_FORMAT)

            EVENTS.insert_one(new_event)
            print(new_event)
            consumer.commit()

    except Exception as e:
        print(e)
        consumer.close()

if __name__ == '__main__':
    main()