#!/usr/bin/python
from kafka import KafkaClient,SimpleProducer
kf_client = KafkaClient("localhost:9092")
topic_name = "awesomefeeds"
msg = "ack request msg.."
producer = SimpleProducer(kf_client,req_acks=SimpleProducer.ACK_AFTER_LOCAL_WRITE)
resp = producer.send_messages(topic_name,msg)
print 'Response',resp

