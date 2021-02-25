# Main IoT Server Raspberry Pi
# Listen Socket Data, and transfer other IoT
import socket

HOST = "192.168.0.11"
PORT = 43210

print("Socket Created")

# Using _Ipv4 (Addreess family) and _TCP (Socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind((HOST,PORT))
server_socket.listen(100)

cilent_socket, addr = server_socket.accept()

print("Connected by", addr)

while True:
    data = cilent_socket.recv(1024)

    #if not data:
    #    break

    print("Received from", addr, " : ", data.decode())

    if data.decode() == "Hello":
        print("Iot No.1 Message Received")

    cilent_socket.sendall(data)

cilent_socket.close()
server_socket.close()
