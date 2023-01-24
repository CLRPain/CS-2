from fltk import *
import socket 
import sys
from pickle import dumps, loads
#python3 battleship.py server/client localhost port

class Battleship(Fl_Window):
    def __init__(self, x, y, width, height, label):
        Fl_Window.__init__(self, x, y, width, height, label)
        self.begin()
        self.ownButList = []
        self.otherButList = []
        self.shipLocation = []
        self.othershiploc = []
        self.shipsSunk = 0
        self.ownShipSunk = 0
        self.blankImage = Fl_PNG_Image('blank.png').copy(60, 60)
        self.hitImage = Fl_PNG_Image('hit.png').copy(60, 60)
        self.missImage = Fl_PNG_Image('miss.png').copy(60, 60)
        self.shipImage = Fl_PNG_Image('ship.png').copy(60, 60)
        
        for col in range(5): #own board
            for row in range(5):
                self.ownButList.append(Fl_Button(col*60+60, row*60+60, 60, 60))
                self.ownButList[-1].callback(self.placeShips)
                self.ownButList[-1].image(self.blankImage)

        for col2 in range(5): #opponent board
            for row2 in range(5):
                self.otherButList.append(Fl_Button(col2*60+420,row2*60+60, 60,60))
                self.otherButList[-1].callback(self.shoot)
                self.otherButList[-1].image(self.blankImage)
                self.otherButList[-1].deactivate()
        
        for x in range(1, 6): #side labels
            Fl_Box(x*60,0, 60,60).label(chr(64+x))
            Fl_Box(x*60+360,0, 60,60).label(chr(64+x))
            
        for y in range(5): #side labels
            Fl_Box(0,60+y*60, 60,60).label(str(y+1))
            Fl_Box(360,60+y*60, 60,60).label(str(y+1))
            
        self.readyBut = Fl_Button(60, 400, 60, 60, 'Ready')
        self.readyBut.callback(self.isReady)
        self.out = Fl_Output(420, 400, 200, 30) #outputs turns and connections
            
        self.end()
            
        self.startConnections()
        self.callback(self.close) 


    def startConnections(self): 
        #creates tcp connection
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = sys.argv[2]
        port = int(sys.argv[3])
        self.out.value('Connection Started')

        if sys.argv[1] == 'server':
            self.s.bind((host, port))
            self.s.listen()
            #finds file descriptor to add (fd of s)
            self.fdl = self.s.fileno()
            Fl.add_fd(self.fdl, self.acceptConnections)
            self.turn = False
            
        elif sys.argv[1] == 'client':
            self.s.connect((host, port))
            #finds file descriptor to add 
            self.fd = self.s.fileno()
            Fl.add_fd(self.fd, self.receive)
            self.turn = True
            self.out.value('Connection Accepted')

    
    def acceptConnections(self, fdl):
        #finds file descriptor to add (fd of self.conn)
        self.conn, addr = self.s.accept()
        self.out.value('Connection Accepted')
        self.fd = self.conn.fileno()
        Fl.add_fd(self.fd, self.receive)
        
        
    def placeShips(self, wid):
        #allows placement for 5 ships and no overlap
        if len(self.shipLocation) < 5 and self.ownButList.index(wid) not in self.shipLocation:
            wid.image(self.shipImage)
            wid.redraw()
            self.shipLocation.append(self.ownButList.index(wid))
    
        
    def isReady(self, wid):
        #checks if there are 5 ships
        if len(self.shipLocation) == 5:
            L = dumps(self.shipLocation)
            #sends list of ships to other
            if sys.argv[1] == 'server':
                self.conn.sendall(L)
                
            elif sys.argv[1] == 'client':
                self.s.sendall(L)
            self.out.value('waiting for other...')
            
            self.onOff()
            self.readyBut.deactivate()
            
        else:
            print(f'Not enough ships. Place {5 - len(self.shipLocation)} more ship(s)')
            
            
    def onOff(self):
        #activate/deactivates depending on turn
        if self.turn == True:
            for but in self.otherButList:
                but.activate()
            self.out.value('Your Turn')
                
        if self.turn == False: #server
            for but in self.otherButList:
                but.deactivate()
               
                
    def shoot(self, wid):
        loc = self.otherButList.index(wid)
        #prevents shots if its not their turn or the other side isnt ready yet
        if self.turn == False or len(self.othershiploc) == 0:
            return
        self.turn = False
        self.sendData(loc)
        #checks if it is a hit or not
        if loc in self.othershiploc:
            wid.image(self.hitImage)
            self.shipsSunk += 1
            self.endingCondition()
        else:
            wid.image(self.missImage)
        wid.redraw()
        self.end()
        #stops shots in the same spot
        wid.callback(None)
        self.onOff()
        self.out.value('Opponent Turn')

            
    def receive(self, fd):
        try:
            loc = self.recvData()
            loc = loads(loc)
            #only the ship locations are in a list
            if type(loc) == list:
                self.othershiploc = loc
                return
            self.turn = True
            #checks if hit or not
            if loc in self.shipLocation:
                self.ownButList[loc].image(self.hitImage)
                self.ownShipSunk += 1
            else:
                self.ownButList[loc].image(self.missImage)
            self.ownButList[loc].redraw()
            #checks if they win, lose, or continue
            self.endingCondition()
            self.onOff()
            self.out.value('Your Turn')
        except:
            #closes connection if window is closed
            self.close(1)
    
    
    def endingCondition(self):
        #checks if you sunk 5 ships
        if self.shipsSunk == 5:
            fl_message('winning')
            for but in self.ownButList:
                but.deactivate()
            for but in self.otherButList:
                but.deactivate()
            self.close(1)
        #checks if your ships are all sunk
        if self.ownShipSunk == 5:
            fl_message('lose')
            for but in self.ownButList:
                but.deactivate()
            for but in self.otherButList:
                but.deactivate()
            self.close(1)
                     
            
    def sendData(self, data):
        #function to send data 
        data = dumps(data)
        if sys.argv[1] == 'client':
            self.s.sendall(data)
        elif sys.argv[1] == 'server':
            self.conn.sendall(data)
            
            
    def recvData(self):
        #function to receive data
        if sys.argv[1] == 'client':
            data = self.s.recv(1024)
        elif sys.argv[1] == 'server':
            data = self.conn.recv(1024)
        return data
        
        
    def close(self, wid):
        #closes the connections without creating errors
        try:
            if sys.argv[1] == 'client':
                self.conn.close()
            else:
                self.s.close()
                Fl.remove_fd(self.fdl)
            Fl.remove_fd(self.fd)
        except:
            print('closing without a connection')
        finally:
            self.hide()
        
if __name__ == "__main__":
    gameSelf = Battleship(0, 0, 780, 500, sys.argv[1])
    gameSelf.show()
    Fl.run()