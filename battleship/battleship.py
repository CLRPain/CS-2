from fltk import *
import socket 
import sys
#python3 battleship.py server/client localhost port

class BattleshipSelf(Fl_Window):
    def __init__(self, x, y, width, height, label):
        Fl_Window.__init__(self, width, height, label)
        self.begin()
        self.ownBL = []
        self.otherBL = []
        self.shiploc = []
        
        
        for col in range(5):
            for row in range(5):
                self.ownBL.append(Fl_Button(col*60+60,row*60+60, 60,60))
                self.ownBL[-1].callback(self.own_cb)
                self.otherBL.append(Fl_Button(col*60+420,row*60+60, 60,60))
                self.otherBL[-1].callback(self.other_cb)
                
        for x in range(1, 6):
            Fl_Box(x*60,0, 60,60).label(chr(64+x))
            Fl_Box(x*60+360,0, 60,60).label(chr(64+x))
            
        for y in range(5):
            Fl_Box(0,60+y*60, 60,60).label(str(y+1))
            Fl_Box(360,60+y*60, 60,60).label(str(y+1))
            
            
        self.end()
            
        self.resizable(self)
        
        self.connect()

        
    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost' #sys.argv[2]
        port = 5555 #int(sys.argv[3])

        if sys.argv[1] == 'server':
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
            s.listen(1)
            self.conn, addr = s.accept()
            self.conn.sendall('Connected to Client'.encode())
            print(self.conn.recv(1024).decode())
            
        elif sys.argv[1] == 'client':
            s.connect((host, port))
            s.sendall('Connected to Server'.encode())
            print(s.recv(1024).decode())
            self.conn = s
        else:
            print('how did you mess up spelling client/server')
        
    def own_cb(self, wid):
        if len(self.shiploc) < 4 and wid.label() == None:
            wid.label('s')
            self.shiploc.append(self.ownBL.index(wid))
            print(self.shiploc)
            
            if len(self.shiploc) == 4:
                print('shot')
                #self.conn.setblocking(False)
                self.shot()
    
    def other_cb(self, wid):
        loc = self.otherBL.index(wid)
        self.conn.send(str(loc).encode())
        print(loc)
        
    def shot(self):
        while True:
            loc = self.conn.recv(1024)
            if int(loc.decode()) in self.shiploc:
                self.LB[loc.decode()].label('h')
        
        
if __name__ == "__main__":
    #gameSelf = BattleshipSelf(0, 0, 360, 360, sys.argv[1])
    gameSelf = BattleshipSelf(0, 0, 780, 500, None)
    gameSelf.show()
    Fl.run()
