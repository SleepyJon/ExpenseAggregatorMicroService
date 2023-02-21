#Description: Expense Aggregator Server

import time
import zmq
import pandas as pd

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8000")
print(f"Expense Aggregator Microservice Server Started")

while True:
    #  Wait for next request from client
    message = socket.recv()
    time.sleep(1)
    print(f"Received request: {message}")
    message = message.decode('utf-8')

    df = pd.read_csv(message, names=["Account No","Date","Transaction Details","Category","Amount"])
    time.sleep(3)
    print("Bank Statement Read")
    
    df2 = df.groupby("Category")["Amount"].sum()
    time.sleep(1)

    df2.to_csv("bank_by_category.csv")
    time.sleep(3)

    print("Bank Statement Processed and saved to bank_by_category.csv")
    time.sleep(3)
    

    #  Send reply back to client
    socket.send_string("Bank Statement Processed")