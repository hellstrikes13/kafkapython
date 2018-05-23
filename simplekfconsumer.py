#!/usr/bin/python
from kafka import KafkaClient,SimpleConsumer
kf_client = KafkaClient("localhost:9092")
topic_name = "awesomefeeds"
consumer_grp= "my_consumer_group"
consumer = SimpleConsumer(kf_client,consumer_grp,topic_name)
for msg in consumer:
    print msg
