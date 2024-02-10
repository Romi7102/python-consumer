import json
from datetime import datetime
from kafka import KafkaConsumer
from pymongo import MongoClient 

def main():
    #! enviroment variables change me !
    bootstrap_servers = 'localhost:9092'
    kafka_topic = 'pyTest'
    
    consumer = KafkaConsumer(kafka_topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')
    
    try:
        consumer.subscribe(['pyTest'])

        for message in consumer:
            json_str = message.value.decode('utf-8')
            insert_mongo(json_str)

    except KeyboardInterrupt:
        consumer.close()

def insert_mongo(json_str : str):

    mongo_cs = 'mongodb://admin:admin@localhost:27017'
    mongo_client = MongoClient(mongo_cs)
    db = mongo_client.testdb
    events = db.events

    most_recent_doc = events.find_one({}, sort=[("timestamp", -1)])

    if most_recent_doc is not None: 
        most_recent_date = most_recent_doc["timestamp"]

    new_event = json.loads(json_str)
    new_event["timestamp"] = datetime.strptime(new_event["timestamp"] ,"%Y-%m-%d %H:%M:%S")

    if most_recent_doc is None or new_event["timestamp"] > most_recent_date:
        events.insert_one(new_event)
        print(new_event)
        



if __name__ == '__main__':
    main()