#tcp client: serializing python objects over network
import socket, pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.7'
port = 4444
s.connect( (host, port) )

L=[('B','N'), (3,5), 'the end', (1.4,2.3,3.0)]
data = pickle.dumps(L)
s.sendall(data)
try:
    L2 = pickle.loads(s.recv(1024))
    print('Server sends modified list:')
    print(L2)
except pickle.UnpicklingError:
    print('Error: 1024 bytes read buffer is too small. Increase buffer size')
finally:
    s.close()
