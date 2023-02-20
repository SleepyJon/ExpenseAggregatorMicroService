#Description: Expense Aggregator Client

import zmq
import os
from datetime import datetime
import time

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:8000")
print(f"Expense Aggregator Microservice Client Started")

#  Do 10 requests, waiting each time for a response
modifiedDate = "first"

while True:
    if os.path.exists('bank.csv') and modifiedDate == 'first':
        time.sleep(3)
        print(f"Bank Statement File Loaded")
        lastModified = os.path.getmtime('bank.csv')
        modifiedDate = lastModified
        time.sleep(3)
        print(f"Sending request to Expense Aggregator Microservice")
        socket.send_string("Requesting Expense Aggregator") 

        #  Get the reply.
        message = socket.recv()
        print(f"Received reply [ {message} ]")

    elif os.path.exists('bank.csv') and modifiedDate != 'first':
        lastModified = os.path.getmtime('bank.csv')
        if lastModified > modifiedDate:
            modifiedDate = lastModified
            print(f"New Bank Statement Detected")
            time.sleep(3)
            print(f"Sending request to Expense Aggregator Microservice")
            socket.send_string("Requesting Expense Aggregator") 

            #  Get the reply.
            message = socket.recv()
            print(f"Received reply [ {message} ]")
    