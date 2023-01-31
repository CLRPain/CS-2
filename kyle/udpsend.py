#CLIENT-send udp
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = sys.argv[1]
port = int(sys.argv[2])

line=input('type message: ') #send only once ===blocking

line=line.encode()
s.sendto( line, (host, port))
