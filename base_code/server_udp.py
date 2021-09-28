import socket

HOST = "192.168.0.11"
PORT = 43210

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server.bind((HOST,PORT))

while True:
    data, addr  = socket_server.recvfrom(1024)
    print("Received ", data.decode(), " ", addr)

    if data.decode()=="STOP":
        break 

socket_server.close()
