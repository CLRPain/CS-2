#server-receive  tcp
import socket, sys

#a socket is a pipe that connects to a port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Address Family_ Internet TCP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# so we can keep using the same port without waiting (optional)
host = '0.0.0.0' #or 0.0.0.0 when using the real network
port = int(sys.argv[1])
s.bind( (host, port) ) #bind to port 3339 because we are receiving
s.listen(1) #the number of allowed pending connections

print('before accept')
conn, addr = s.accept()
#blocking (same as input but instead waits for an incoming connection)
print('after accept')
print('conn = ', conn)
print('addr = ', addr)
data=True
while True:
    data = conn.recv(1024)
    # also blocking but now for data from the established connection
    print(data.decode())
    if data.decode() == 'q':
        break
conn.close()
