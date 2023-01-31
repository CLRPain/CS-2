#server-receive  tcp
import socket, sys,os

print('server pid:',os.getpid())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = sys.argv[1]
port= int(sys.argv[2])
s.bind( (host, port) )
s.listen(1)
print(s)
print()
conn, addr = s.accept()
print(conn)
while True:
    reply = input("Send: ")
    conn.sendall(reply.encode())
    if reply == 'bye':
        break
    data = conn.recv(1024)
    print('Client says: ',data.decode())

conn.close()
