#Description: Expense Aggregator Client

import zmq
import time

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:8000")
print(f"Expense Aggregator Microservice Client Started")


def getFilePath():
    passedFilePath = input("Please enter file path of bank statement to process: ")
    return passedFilePath


while True:
    filePath = "StandBy"
    filePath = getFilePath()

    if filePath != "StandBy":
        time.sleep(1)
        print(f"Sending request to Expense Aggregator Microservice")
        socket.send(filePath.encode())

        #  Get the reply.
        message = socket.recv()
        time.sleep(3)
        print(f"Received reply [ {message} ]")
        time.sleep(5)

