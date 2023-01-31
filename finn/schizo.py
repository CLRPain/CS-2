import socket,sys
from fltk import *
# 3 args (client/server) host port
#usage: python program.py  server localhost 5555
#usage: python program.py  client localhost 5555
#remember machine to machine, host = 0.0.0.0

class udpwin(Fl_Window):
    def __init__(self,x,y,w,h,label):
        Fl_Window.__init__(self,x,y,w,h,label)
        self.begin()
        self.inp=Fl_Input(50,80,300,40,"type")
        self.brow=Fl_Multi_Browser(50,180,300,150)
        self.end()
        self.inp.when(FL_WHEN_ENTER_KEY)
        self.inp.callback(self.send_cb)
        self.host = sys.argv[2]
        self.port=int(sys.argv[3])
        self.s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        if sys.argv[1] == "server":
            self.s.bind((self.host, self.port)) # servers bind

        fd=self.s.fileno()
        print(fd)
        '''
        fd or a file descriptor is an integer the OS uses
        to reference the socket.
        '''
        Fl.add_fd( fd, self.receive_data)
        '''
        an fltk function which watches the fd during the
        event loop. If any data is received by that socket
        then function "receive_data" is called
        '''

    def send_cb(self, widget): #server receives before sending
        text=self.inp.value()
        if sys.argv[1] == "server":
            self.s.sendto(text.encode(), self.addr) #server
        else: #client
            self.s.sendto(text.encode(),(self.host,self.port))

    def receive_data(self, fd):
        (text, self.addr)=self.s.recvfrom(1024)
        self.brow.add(text.decode())

a=udpwin(55,55,400,400,"sockets "+sys.argv[1])
a.show()
Fl.run()
