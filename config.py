import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

BOOTSTRAP_SERVER = config["BOOTSTRAP_SERVER"]
TOPIC = config["TOPIC"]
KAFKA_GROUP_ID = config["KAFKA_GROUP_ID"]
MONGO_CS = config["MONGO_CS"]
MONGO_DB = config["MONGO_DB"]
MONGO_COLLECTION = config["MONGO_COLLECTION"]
ENCODING = config["ENCODING"]
DATETIME_FORMAT = config["DATETIME_FORMAT"]