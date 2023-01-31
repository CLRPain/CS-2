# tcp server: serializing python objects over network
import socket, pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = '0.0.0.0'
port= 4444
s.bind( (host, port) )
s.listen(1)
conn, addr = s.accept()
try:
    #must be sure that object fits in 1024 bytes
    L = pickle.loads(conn.recv(1024))
    print(f'{addr[0]} sends object of type  {type(L)}')
    print(L)
    L.append({'a':3, 'c':9})
    data=pickle.dumps(L)
    conn.sendall(data)
except pickle.UnpicklingError:
    print('Error: 1024 bytes read buffer is too small.Increase buffer size')
finally:
    conn.close()
