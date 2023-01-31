#CLIENT-send tcp
import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp sock_stream
host = sys.argv[1] #or localhost if on same machine
port = int(sys.argv[2])
s.connect( (host, port) ) # unblocks s.accept on reciever

line = input('Send :') #blocking, waits for user input

s.send(line.encode()) #unblocks conn.recv on receiver
#In tcp connections packets don't have to arrive in order.
#also no guarantee that all data
#is transmitted until connection is closed or use sendall

s.close() #this garantees that all packets are sent
