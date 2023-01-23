from fltk import *
import socket 
import sys
import pickle as p
import threading as th
#python3 battleship.py server/client localhost port

class BattleshipSelf(Fl_Window):
    def __init__(self, x, y, width, height, label):
        Fl_Window.__init__(self, x, y, width, height, label)
        self.begin()
        self.ownBL = []
        self.otherBL = []
        self.shiploc = []
        self.shotloc = []
        self.shiphits = 0
        self.blank = Fl_PNG_Image('blank.png').copy(60, 60)
        self.hit = Fl_PNG_Image('hit.png').copy(60, 60)
        self.miss = Fl_PNG_Image('miss.png').copy(60, 60)
        self.ship = Fl_PNG_Image('ship.png').copy(60, 60)
        
        
        for col in range(5):
            for row in range(5):
                self.ownBL.append(Fl_Button(col*60+60,row*60+60, 60,60))
                self.ownBL[-1].callback(self.place)
                self.ownBL[-1].image(self.blank)

        for col2 in range(5):
            for row2 in range(5):
                self.otherBL.append(Fl_Button(col2*60+420,row2*60+60, 60,60))
                self.otherBL[-1].callback(self.shoot)
                self.otherBL[-1].image(self.blank)
                self.otherBL[-1].deactivate()
        
        for x in range(1, 6):
            Fl_Box(x*60,0, 60,60).label(chr(64+x))
            Fl_Box(x*60+360,0, 60,60).label(chr(64+x))
            
        for y in range(5):
            Fl_Box(0,60+y*60, 60,60).label(str(y+1))
            Fl_Box(360,60+y*60, 60,60).label(str(y+1))
            
        self.readybut = Fl_Button(60, 450, 60, 60, 'Ready?')
        self.readybut.callback(self.ready)
            
        self.end()
            
        self.resizable(self)
        self.connect()
        

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost' #sys.argv[2]
        port = 25565 #int(sys.argv[3])

        if sys.argv[1] == 'server':
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
            s.listen(1)
            self.conn, addr = s.accept()
            
        elif sys.argv[1] == 'client':
            s.connect((host, port))
            self.conn = s
        else:
            print('how did you mess up spelling client/server')
    
    
    def place(self, wid):
        if len(self.shiploc) < 5 and self.ownBL.index(wid) not in self.shiploc:
            wid.image(self.ship)
            wid.redraw()
            self.shiploc.append(self.ownBL.index(wid))
    
        
    def ready(self, wid):
        if len(self.shiploc) == 5:
            L = p.dumps(self.shiploc)
            if sys.argv[1] == 'server':
                self.othershiploc = p.loads(self.conn.recv(1024))
                self.conn.send(L)
                self.turn = False
                self.receive()
                
            elif sys.argv[1] == 'client':
                self.conn.send(L)
                self.othershiploc = p.loads(self.conn.recv(1024))
                self.turn = True
            
            self.onoff()
            
        else:
            print(f'Not enough ships. Place {5 - len(self.shiploc)} more ship(s)')
            
    def onoff(self):
        if self.turn == True:
            for but in self.otherBL:
                but.activate()
                
        if self.turn == False: #server
            for but in self.otherBL:
                but.deactivate()
            self.receive()
                
    def shoot(self, wid):
        loc = self.otherBL.index(wid)
        if loc not in self.shotloc:
            self.shotloc.append(loc)
            self.conn.send(str(loc).encode())
            if loc in self.othershiploc:
                self.otherBL[loc].image(self.hit)
                self.shiphits += 1
            else:
                self.otherBL[loc].image(self.miss)
            self.otherBL[loc].redraw()
            self.turn = False
            self.end()
            self.onoff()

            
    def receive(self):
        loc = self.conn.recv(1024)
        loc = int(loc.decode())
        if loc in self.shiploc:
            self.ownBL[loc].image(self.hit)
        else:
            self.ownBL[loc].image(self.miss)
        self.ownBL[loc].redraw()
        self.turn = True
        self.onoff()
    
    
    def end(self):
        if self.shiphits == 5:
            fl_message('winning')
            
        
if __name__ == "__main__":
    try:
        gameSelf = BattleshipSelf(0, 0, 780, 500, sys.argv[1])
        gameSelf.show()
        Fl.run()
    except Exception as e:
        print(e)
        gameSelf.close()