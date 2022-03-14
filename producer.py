#!/usr/bin/env python

from confluent_kafka import Producer
from datetime import datetime
from dateutil.tz import tzutc

# Load data to send from file
# read line-by-line, one message per line
in_file = open('data.txt','r')
data_source = in_file.readlines()

p = Producer({'bootstrap.servers': 'localhost:29092'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

count = 0
for data in data_source:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    count += 1
    # Add id info to the meesages
    data = "[" + datetime.now(tzutc()).isoformat() + "] " + str(count) + ": " + data
    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()