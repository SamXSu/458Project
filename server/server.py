from socket import *
from ssl import *
from _ssl import PROTOCOL_TLSv1

server_socket = socket(AF_INET, SOCK_STREAM)

address = 'localhost'
port = 6668
bufsize = 1024

server_socket.bind((address, port))

server_socket.listen(1)
tls_server = wrap_socket(server_socket, 
                         ssl_version=PROTOCOL_TLSv1, 
                         cert_reqs=CERT_NONE, 
                         server_side=True, 
                         keyfile='./keyfile.pem',
                         certfile='./certfile.pem')

print('Server Started')

connection, client_address = tls_server.accept()
print('Connection from', client_address)

finished = False

while not finished:
    data_in = connection.recv(bufsize)
    message = data_in.decode()
    print('Client send', message)
    
    if message == 'quit':
        finished = True
        
connection.shutdown(SHUT_RDWR)
connection.close()

server_socket.shutdown(SHUT_RDWR)
server_socket.close()