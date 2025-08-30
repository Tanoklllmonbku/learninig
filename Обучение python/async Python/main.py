import socket
import asyncio
from select import select

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
serv.bind(('localhost', 55000))

serv.listen()

def accept_conn(serv):
    while True:
        client_sock, addr = serv.accept()
        print(addr)
        send_mess(client_sock)

def send_mess(client_sock):
    while True:
        request = client_sock.recv(4096)
        print(request)
        if not request:
            break
        else:
            response = 'Hi!'.encode()
            client_sock.send(response)
    client_sock.close()

def event_loop():
    while True:


if __name__ == '__main__':
    accept_conn(serv)