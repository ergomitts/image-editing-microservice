import zmq 
import json 
import os

PORT = 1739

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://localhost:{PORT}")
    socket.send_json({
        "command": "load",
        "path": "photo.jpg"
    })
    response = socket.recv_json()
    print(f"Received reply: {response}") 
    socket.send_json({
        "command": "resize",
        "width": "500",
        "height": "500"
    })
    response = socket.recv_json()
    print(f"Received reply: {response}") 
    socket.send_json({
        "command": "monochrome"
    })
    response = socket.recv_json()
    print(f"Received reply: {response}") 

if __name__ == "__main__":
    main()