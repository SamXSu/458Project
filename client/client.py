from socket import *
from ssl import *
from _ssl import PROTOCOL_TLSv1

finished = False

client_socket = socket(AF_INET, SOCK_STREAM)
tls_client = wrap_socket(client_socket, 
                         ssl_version=PROTOCOL_TLSv1, 
                         cert_reqs=CERT_NONE)

address = 'localhost'
port = 6668
bufsize = 1024

tls_client.connect((address, port))

while not finished:
    message = 'Hello World!'
    data_out = message.encode(encoding='utf_8', errors='strict')
    tls_client.send(data_out)
    
    repeat = input('yes or no?')
    
    if repeat == 'n':
        finished = True
        client_socket.send(b'quit')
        
client_socket.shutdown(SHUT_RDWR)
client_socket.close()