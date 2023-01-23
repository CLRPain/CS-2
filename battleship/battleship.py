from fltk import *
import socket 
import sys
#python3 battleship.py server/client localhost port

class Battleship(Fl_Window):
    def __init__(self, x, y, width, height, label):
        Fl_Window.__init__(self, width, height, label)
        self.begin()
        self.ownButList = []
        self.otherButList = []
        self.shipLocations = []
        self.blankImage = Fl_PNG_Image('blank.png').copy(60, 60)
        self.hitImage = Fl_PNG_Image('hit.png').copy(60, 60)
        self.missImage = Fl_PNG_Image('miss.png').copy(60, 60)
        self.shipImage = Fl_PNG_Image('ship.png').copy(60, 60)
        
        
        for col in range(5):
            for row in range(5):
                self.ownButList.append(Fl_Button(col*60+60, row*60+60, 60, 60))
                self.ownButList[-1].callback(self.placeShips)
                self.ownButList[-1].image(self.blankImage)
                self.otherButList.append(Fl_Button(col*60+420, row*60+60, 60, 60))
                self.otherButList[-1].callback(self.other_cb)
                self.otherButList[-1].image(self.blankImage)
                
        for x in range(1, 6):
            Fl_Box(x*60,0, 60, 60).label(chr(64+x))
            Fl_Box(x*60+360, 0, 60, 60).label(chr(64+x))
            
        for y in range(5):
            Fl_Box(0, 60+y*60, 60, 60).label(str(y+1))
            Fl_Box(360, 60+y*60, 60, 60).label(str(y+1))
            
        self.readybut = Fl_Button(60, 450, 60, 60, 'Ready')
            
            
        self.end()
            
        self.resizable(self)
        self.startConnections()
        

        
    def startConnections(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = sys.argv[2]
        port = int(sys.argv[3])

        if sys.argv[1] == 'server':
            self.s.bind((host, port))
            self.s.listen()
            self.fdl = self.s.fileno()
            Fl.add_fd(self.fdl, self.acceptConnections)
            
        elif sys.argv[1] == 'client':
            self.s.connect((host, port))
            self.fd = self.s.fileno()
            Fl.add_fd(self.fd, self.recieve)
            
    def acceptConnections(self, fd):
        self.conn, addr = self.s.accept()
        self.fd = self.conn.fileno()
        Fl.add_fd(self.fd, self.recieve)
        
        
    def placeShips(self, wid):
        if len(self.shipLocations) < 5 and wid.label() == None:
            wid.label('s')
            self.shipLocations.append(self.ownButList.index(wid))
            print(self.shipLocations)
    
    def other_cb(self, wid):
        loc = self.otherButList.index(wid)
        sent = self.conn.sendall(str(loc).encode())
        self.recv = self.conn.recv(1024)
        print(sent, 'if None == success')
        
        
    def ready(self):
        if len(self.shipLocations) == 5:
            self.conn.sendall('Ready')
    
            
        else:
            print(f'Not enough ships. Place {5 - len(self.shipLocations)} more ship(s)')
            
            
    def shot(self):
        #while len(self.shiploc) != 0:
        print('shotted')
        loc = self.conn.recv(1024)
        loc = int(loc.decode())
        print(loc, 'here')
        if loc in self.shipLocations:
            self.ownButList[loc].label('h')
            self.shipLocations.remove(loc)
        self.shot()
        
        
if __name__ == "__main__":
    gameSelf = Battleship(0, 0, 780, 500, sys.argv[1])
    #gameSelf = BattleshipSelf(0, 0, 780, 500, None)
    gameSelf.show()
    Fl.run()
