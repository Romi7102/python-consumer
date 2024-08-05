# python-consumer
This project is a Kafka consumer written in Python using the kafka-python library. It subscribes to a Kafka topic and inserts all JSON messages into a MongoDB database.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Clone this repository:

    ```git clone https://github.com/Romi7102/python-consumer.git```

2. Install the required dependencies: (required for none docker usage)
    
    ``` pip install -r requirements.txt```


## Usage

1. Ensure that you have a running Kafka cluster and a MongoDB instance.

2. Fill the yaml configuration with the following values:
    
    BOOTSTRAP_SERVER: Specifies the bootstrap servers for your Kafka cluster. These are used by the Kafka consumer to initially establish connections with the Kafka brokers in the cluster

    TOPIC: Specifies the Kafka topic that the Kafka consumer will subscribe to. The consumer will receive messages from this topic and process them accordingly.

    KAFKA_GROUP_ID: Specifies the Kafka group ID that will be used.

    MONGO_CS: Specifies the connection URI for your MongoDB database. It should include the protocol (e.g., mongodb://), hostname, port number, and any authentication credentials if required.

    MONGO_DB: Specifies the database to connect to. 

    MONGO_COLLECTION: Specifies the collection to pull data from.

    ENCODING: Specifies the json encoding of the data returned from the server.

    DATETIME_FORMAT: Specifies the date format of the data returned from the server. 

3. Build the docker image using the dokcer file

    ```dokcer build -t python-consumer .```

4. Run the image with the following command:

   `docker run python-cosumer`


## Running without docker

Alternatively, you can run the project locally. like stated in the [Installation](#installation) instructions , start with installing the requirements from the requirements.txt file with the following command:

`pip install -r requirements.txt`

Then provide the configuration to the config.yaml file the same way you would if running in docker.

Finally, run the main.py file with the following command:

`python main.py`
