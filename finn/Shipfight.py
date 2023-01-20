import socket
from fltk import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if sys.argv[1] == "client":
    type = "Client"
    s.settimeout(5.0)
    host = sys.argv[2]
    port = int(sys.argv[3])
    s.connect( (host, port) )
    """
    while True:
        pshot, con = s.recv(1024)
        pshot.decode()
        #if con.decode() == True:
        print("Hi")
    """
if sys.argv[1] == "server":
    type = "Server"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = sys.argv[2]
    port = int(sys.argv[3])
    s.bind( (host, port) )
    s.listen(1)
    conn, addr = s.accept()
    """
    while True:
        pshot, con = conn.recv(1024)
        pshot.decode()
        #if con.decode() == True:
        print("Hi")
    """


class Home(Fl_Window):
    abl = {}
    bl = {}
    sl = {}
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
                 
        for x in range(5):
            box = Fl_Box(0,25 + 75*x,25,75, chr(65+x))
        for x in range(5):
            box = Fl_Box(25 + 75*x,0,75,25, str(x + 1))
        for x in range(5):
            box = Fl_Box(0,425 + 75*x,25,75, chr(65+x))
        for x in range(5):
            box = Fl_Box(25 + 75*x,400,75,25, str(x + 1))
        self.resizable(self)    
            
            
    def ship(self, wid, coord):
        self.boats -= 1
        if self.boats >= 0:
            self.sl[coord] = wid
            wid.image(self.boatimg)
            wid.deactivate()
            if self.boats == 0:
                for y in range(5):
                    for x in range(5):
                        self.bl[x,y].deactivate()
                        if type == "Server":
                            conn.send('Ready'.encode())
                            data = conn.recv(1024).decode()
                            if data == 'Ready':
                                for y in range(5):
                                    for x in range(5):
                                        coord = (x,y)
                                        self.abl[coord].callback(self.shoot, coord)
                                        
                        else:
                            data = s.recv(1024).decode()
                            s.send('Ready'.encode())
                            if data == 'Ready':
                                for y in range(5):
                                    for x in range(5):
                                        coord = (x,y)
                                        self.abl[coord].callback(self.shoot, coord)

    def shoot(self, wid, coord):
        if type == "Server" and self.sturn == True:
            self.sturn = False
            shot = coord
            conn.sendall(shot.encode(), self.sturn.encode())
        if type == "Client" and self.sturn == False:
            self.sturn = True
            shot = coord
            s.sendall(shot.encode(), self.sturn.encode())

        
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
