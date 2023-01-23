import socket
from fltk import *
import sys
import pickle


if sys.argv[1] == "client":
    type = "Client"
if sys.argv[1] == "server":
    type = "Server"

class Home(Fl_Window):
    abl = {}
    bl = {}
    sl = {}
    sl2 = []
    hits = 0
    sturn = True
    hit = False
    boats = 5
    def __init__(self, w, h, label = None):
        Fl_Window.__init__(self, w, h, label)
        blankimg = Fl_PNG_Image("blank.png")
        blankimg = blankimg.copy(75,75)
        boatimg = Fl_PNG_Image("ship.png")
        self.boatimg = boatimg.copy(75,75)
        hitimg = Fl_PNG_Image("hit.png")
        self.hitimg = hitimg.copy(75,75)
        missimg = Fl_PNG_Image("miss.png")
        self.missimg = missimg.copy(75,75)
        self.unite()
        
        for y in range(5):
            for x in range(5):
                but = Fl_Button(25 + 75*x,25 + 75*y,75,75)
                coord = (x,y)
                but.callback(self.ship, coord)
                but.image(blankimg)
                self.bl[coord] = but
        
        for y in range(5):
            for x in range(5):
                but = Fl_Button(25 + 75*x,425 + 75*y,75,75)
                coord = (x,y)
                but.image(blankimg)
                self.abl[coord] = but
                but.callback(self.fire, coord)
                 
        for x in range(5):
            box = Fl_Box(0,25 + 75*x,25,75, chr(65+x))
        for x in range(5):
            box = Fl_Box(25 + 75*x,0,75,25, str(x + 1))
        for x in range(5):
            box = Fl_Box(0,425 + 75*x,25,75, chr(65+x))
        for x in range(5):
            box = Fl_Box(25 + 75*x,400,75,25, str(x + 1))
        self.resizable(self)
        

    def unite(self):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if type == "Client":
            s.settimeout(5.0)
            host = sys.argv[2]
            port = int(sys.argv[3])
            s.connect( (host, port) )
            self.conn = s
            return s

        if type == "Server":
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            host = sys.argv[2]
            port = int(sys.argv[3])
            s.bind( (host, port) )
            s.listen(1)
            self.conn, addr = s.accept()
        
            
    def ship(self, wid, coord):
        self.boats -= 1
        if self.boats >= 0:
            self.sl[coord] = wid
            self.sl2.append(coord)
            wid.image(self.boatimg)
            wid.deactivate()
            if self.boats == 0:
                for y in range(5):
                    for x in range(5):
                        self.bl[x,y].deactivate()
                if type == "Server":
                    self.conn.send('Ready'.encode())
                    data = self.conn.recv(1024).decode() #server breaks here
                    if data == 'Ready':
                        for y in range(5):
                            for x in range(5):
                                coord = (x,y)
                                self.abl[coord].deactivate()
                        self.sturn()
       
                else:
                    data = self.conn.recv(1024).decode() #client breaks here
                    self.conn.send('Ready'.encode())
                    if data == 'Ready':
                        for y in range(5):
                            for x in range(5):
                                coord = (x,y)
                                self.abl[coord].deactivate()
                        self.sturn()



    def sturn(self):
        if type == "Server":
            self.turn = True
            self.rturn()
            
            
        if type == "Client":
            self.turn = False
            self.rturn()
    
    def rturn(self):
        if self.turn == False:
            self.recieve()
            
        if self.turn == True:
            for y in range(5):
                for x in range(5):
                    coord = (x,y)
                    self.abl[coord].activate()
            


    def recieve(self):
        shot = self.conn.recv(1024)
        shot = pickle.loads(shot)
        #print(self.sl2)
        #print(shot)
        if shot in self.sl2:
            #print("got")
            self.conn.sendall("Hit".encode())
            #print("got2")
            self.bl[shot].activate()
            self.bl[shot].image(self.hitimg)
            self.bl[shot].deactivate()
            self.sl2.remove(shot)
            lc = self.loss()
            if lc == True:
                return
        else:
            self.conn.sendall("Miss".encode())
            self.bl[shot].activate()
            self.bl[shot].image(self.missimg)
            self.bl[shot].deactivate()
        self.turn = True
        self.rturn()

    def fire(self, wid, coord):
        wid.callback(None)
        print("hi")
        coord = pickle.dumps(coord)
        self.conn.sendall(coord)
        con = self.conn.recv(1024)
        con = con.decode()
        if con == "Hit":
            self.hits += 1
            wid.image(self.hitimg)
            wid.redraw()
            wc = self.win()
            if wc == True:
                return
            
        if con == "Miss":
            wid.image(self.missimg)
            wid.redraw()
            
        for y in range(5):
            for x in range(5):
                coord = (x,y)
                self.abl[coord].deactivate()    
        self.turn = False
        self.rturn()
        
    def loss(self):
        if len(self.sl2) == 0:
            fl_message(f"{type} Loses...")
            return True


    def win(self):
        if self.hits == 5:
            fl_message(f"{type} Wins!")
            return True




        
    


    
    


        
"""
self.sl[(0,0)].activate()
self.sl[(0,0)].image(self.hitimg)
self.sl[(0,0)].deactivate()
#if (0,0) in self.sl.keys(): very cool as keys return as a list
#print("hi")
"""    

win = Home(400,800,f"Water Shoot {type}: Home")
win.show()
Fl.run()