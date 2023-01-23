from fltk import *
import socket 
import sys
import pickle as p
#python3 battleship.py server/client localhost port

class Battleship(Fl_Window):
    def __init__(self, x, y, width, height, label):
        Fl_Window.__init__(self, x, y, width, height, label)
        self.begin()
        self.ownButList = []
        self.otherButList = []
        self.shipLocation = []
        self.shotLocation = []
        self.shipsSunk = 0
        self.blankImage = Fl_PNG_Image('blank.png').copy(60, 60)
        self.hitImage = Fl_PNG_Image('hit.png').copy(60, 60)
        self.missImage = Fl_PNG_Image('miss.png').copy(60, 60)
        self.shipImage = Fl_PNG_Image('ship.png').copy(60, 60)
        
        for col in range(5):
            for row in range(5):
                self.ownButList.append(Fl_Button(col*60+60, row*60+60, 60, 60))
                self.ownButList[-1].callback(self.placeShips)
                self.ownButList[-1].image(self.blankImage)

        for col2 in range(5):
            for row2 in range(5):
                self.otherButList.append(Fl_Button(col2*60+420,row2*60+60, 60,60))
                self.otherButList[-1].callback(self.shoot)
                self.otherButList[-1].image(self.blankImage)
                self.otherButList[-1].deactivate()
        
        for x in range(1, 6):
            Fl_Box(x*60,0, 60,60).label(chr(64+x))
            Fl_Box(x*60+360,0, 60,60).label(chr(64+x))
            
        for y in range(5):
            Fl_Box(0,60+y*60, 60,60).label(str(y+1))
            Fl_Box(360,60+y*60, 60,60).label(str(y+1))
            
        self.readyBut = Fl_Button(60, 400, 60, 60, 'Ready')
        self.readyBut.callback(self.isReady)
            
        self.end()
            
        self.resizable(self)
        self.startConnections()
        self.callback(self.close)

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
            self.turn = False
            
        elif sys.argv[1] == 'client':
            self.s.connect((host, port))
            self.fd = self.s.fileno()
            Fl.add_fd(self.fd, self.receive)
            self.turn = True

    
    def acceptConnections(self, fdl):
        self.conn, addr = self.s.accept()
        self.fd = self.conn.fileno()
        Fl.add_fd(self.fd, self.receive)
        
        
    def placeShips(self, wid):
        if len(self.shipLocation) < 5 and self.ownButList.index(wid) not in self.shipLocation:
            wid.image(self.shipImage)
            wid.redraw()
            self.shipLocation.append(self.ownButList.index(wid))
    
        
    def isReady(self, wid):
        if len(self.shipLocation) == 5:
            L = p.dumps(self.shipLocation)
            if sys.argv[1] == 'server':
                self.conn.sendall(L)
                
            elif sys.argv[1] == 'client':
                self.s.sendall(L)
                
            
            self.onOff()
            self.readyBut.deactivate()
            
        else:
            print(f'Not enough ships. Place {5 - len(self.shipLocation)} more ship(s)')
            
            
    def onOff(self):
        if self.turn == True:
            for but in self.otherButList:
                but.activate()
                
        if self.turn == False: #server
            for but in self.otherButList:
                but.deactivate()
               
                
    def shoot(self, wid):
        loc = self.otherButList.index(wid)
        if self.turn == False:
            return
        elif loc not in self.shotLocation:
            self.turn = False
            self.shotLocation.append(loc)
            self.sendData(loc)
            if loc in self.othershiploc:
                wid.image(self.hitImage)
                self.shipsSunk += 1
            else:
                wid.image(self.missImage)
            wid.redraw()
            self.end()
        wid.callback(None)
        self.onOff()

            
    def receive(self, fd):
        loc = self.recvData()
        loc = p.loads(loc)
        if type(loc) == list:
            self.othershiploc = loc
            return
        self.turn = not self.turn
        if loc in self.shipLocation:
            self.ownButList[loc].image(self.hitImage)
        else:
            self.ownButList[loc].image(self.missImage)
        self.ownButList[loc].redraw()
        self.onOff()
    
    
    def endingCondition(self):
        if self.shipsSunk == 5:
            fl_message('winning')
            self.close()
            
            
    def sendData(self, data):
        data = p.dumps(data)
        if sys.argv[1] == 'client':
            self.s.sendall(data)
        elif sys.argv[1] == 'server':
            self.conn.sendall(data)
            
            
    def recvData(self):
        if sys.argv[1] == 'client':
            data = self.s.recv(1024)
        elif sys.argv[1] == 'server':
            data = self.conn.recv(1024)
        return data
        
        
    def close(self, wid):
        try:
            self.conn.close()
        except:
            print('closing without a connection')
        finally:
            self.hide()
        
if __name__ == "__main__":
    try:
        gameSelf = Battleship(0, 0, 780, 500, sys.argv[1])
        gameSelf.show()
        Fl.run()
    except Exception as e:
        print(e)