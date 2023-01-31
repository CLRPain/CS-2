#server-receive  udp
# usage: python3 udprecv.py localhost 5555
#server receives
import socket, sys

#a socket is a pipe that connects to a port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Address Family_ Internet Datagram is udp
host = sys.argv[1]  # host should be localhost or 0.0.0.0
port = int(sys.argv[2])  # min 1025 max 65535
s.bind((host, port))

while True:
    #print('before')
    data, addr = s.recvfrom(1024) # this line blocks
    #print('after')
    data=data.decode()
    if data=='q':
        break
    #print(f'{data} is from {addr}')
    print(data)

