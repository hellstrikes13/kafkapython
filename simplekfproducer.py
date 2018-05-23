#!/usr/bin/python
from kafka import KafkaClient,SimpleProducer
kf_client = KafkaClient("localhost:9092")
topic_name = "awesomefeeds"
msg = "welcome to awesome feeds topics"
producer = SimpleProducer(kf_client)
producer.send_messages(topic_name,msg)
print 'msg',msg,' sent to kafka topic ',topic_name

