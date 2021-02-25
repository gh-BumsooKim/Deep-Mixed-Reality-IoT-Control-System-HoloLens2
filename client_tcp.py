import socket

HOST = "192.168.0.11"  # IPv4 Address
PORT = 43210           # Port Number, using dynamic ports : 49152 ~ 65535
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
 
data = "hello"

client_socket.send(data.encode())
 
data = client_socket.recv(1024)
print("Received", repr(data.decode()))

client_socket.close()
