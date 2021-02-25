import socket

HOST = "192.168.0.11"  # IPv4 Address
PORT = 43210           # Port Number, using dynamic ports : 49152 ~ 65535 

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("Input Data : ")
    
    socket_client.sendto(data.encode(), (HOST,PORT))
    
socket_client.close()
