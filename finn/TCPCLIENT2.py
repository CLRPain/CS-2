#client-send tcp
import socket, sys,os
print('client pid:',os.getpid())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = sys.argv[1]
port = int(sys.argv[2])
s.connect( (host, port) )

while True:
    data = s.recv(1024) 
    print('Server replies: ',data.decode())
    if data.decode() == 'bye':
        print('Server ended call')
        break
    line = input('Send :') 
    s.sendall(line.encode())

   
s.close()
