import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = sys.argv[1]
port = int(sys.argv[2])
s.bind((host, port))
s.listen(1)

conn, addr = s.accept()

while True:
    data=conn.recv(8192)
    print('Says:', data.decode())
    if data.lower() == 'bye':
        conn.sendall('cya'.encode())
        break
    reply = input('Send :')
    conn.sendall(reply.encode())
    if reply.lower() == 'bye':
        break
conn.close()