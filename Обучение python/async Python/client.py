import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 55000))

client_socket.send(b'Hello')
print(client_socket.recv(2048))
