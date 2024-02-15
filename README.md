# python-consumer
This project is a Kafka consumer written in Python using the kafka-python library. It subscribes to a Kafka topic and inserts all JSON messages into a MongoDB database. Each JSON object must include a timestamp in "%Y-%m-%d %H:%M:%S" format.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Clone this repository:

    ```git clone https://github.com/Romi7102/python-consumer.git```

2. Install the required dependencies:
    
    ``` pip install -r requirements.txt```


## Usage

1. Ensure that you have a running Kafka cluster and a MongoDB instance.

2. Build the docker image using the dokcer file

    ```dokcer build -t python-consumer .```

3. Run the image with the following environment variables

    ```docker run -e BOOTSTRAP_SERVER=<kafka server> -e TOPIC=<kafka topic> -e KAFKA_GROUP_ID=<group id> -e MONGO_CS=<mongo connection string> -e MONGO_DB=<database name> -e MONGO_COLLECTION=<collection name> python-consumer```

    ### Environment Variables
    
    BOOTSTRAP_SERVER: This environment variable specifies the bootstrap servers for your Kafka cluster. These are used by the Kafka consumer to initially establish connections with the Kafka brokers in the cluster

    TOPIC: This environment variable specifies the Kafka topic that the Kafka consumer will subscribe to. The consumer will receive messages from this topic and process them accordingly.

    KAFKA_GROUP_ID: This environment variable specifies the Kafka group ID that will be used.

    MONGO_CS: This environment variable specifies the connection URI for your MongoDB database. It should include the protocol (e.g., mongodb://), hostname, port number, and any authentication credentials if required.

    MONGO_DB: This environment variable specifies the database to connect to. 

    MONGO_COLLECTION: This environment variable specifies the collection to pull data from.


## Running without docker

Alternatively, you can run the project locally , you would just need a way to load environment variables so the main.py file will recognize them , you can use any way you see fit.