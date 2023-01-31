#CLIENT-send tcp
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp sock_stream
host = "192.168.3.6" #or localhost if on same machine
port = 3339
s.connect( (host, port) ) # unblocks s.accept on reciever
while True:
    line = input('Send :') #blocking, waits for user input

    s.send(line.encode()) #unblocks conn.recv on receiver
#In tcp connections packets don't have to arrive in order.
#also no guarantee that all data
#is transmitted until connection is closed or use sendall
    if line == 'q':
        break
s.close() #this garantees that all packets are sent
