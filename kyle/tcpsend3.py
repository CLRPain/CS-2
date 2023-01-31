import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = sys.argv[1]
port = int(sys.argv[2])
s.connect((host, port))

while True:
    line = input('Send: ')
    ye = s.sendall(line.encode())
    print(ye, 'a')
    
    data = s.recv(8192)
    print('Reply: ', data.decode())
    if data.decode() == 'bye':
        print('Ended Connection')
        break
    
s.close()