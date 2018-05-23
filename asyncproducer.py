#!/usr/bin/python
from kafka import KafkaClient,SimpleProducer
kf_client = KafkaClient("localhost:9092")
topic_name = "awesomefeeds"
msg = "this is async msg..."
producer = SimpleProducer(kf_client,async=True)
producer.send_messages(topic_name,msg)
print 'msg',msg,' sent to kafka topic ',topic_name

