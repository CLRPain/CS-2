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
    
if sys.argv[1] == "server":
    type = "Server"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = sys.argv[2]
    port = int(sys.argv[3])
    s.bind( (host, port) )
    s.listen(1)
    conn, addr = s.accept()


class Home(Fl_Window):
    bl = {}
    sl = {}
    boats = 5
    def __init__(self, w, h, label = None):
        Fl_Window.__init__(self, w, h, label)
        blankimg = Fl_PNG_Image("blank.png")
        blankimg = blankimg.copy(75,75)
        boatimg = Fl_PNG_Image("ship.png")
        self.boatimg = boatimg.copy(75,75)
        hitimg = Fl_PNG_Image("hit.png")
        self.hitimg = hitimg.copy(75,75)
        for y in range(5):
            for x in range(5):
                but = Fl_Button(25 + 75*x,25 + 75*y,75,75)
                coord = (x,y)
                but.callback(self.ship, coord)
                but.image(blankimg)
                self.bl[coord] = but
                 
        for x in range(5):
            box = Fl_Box(0,25 + 75*x,25,75, chr(65+x))
        for x in range(5):
            box = Fl_Box(25 + 75*x,0,75,25, str(x + 1))
            
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
                #win2 = Attack(0,458,400,400, f"Water Shoot {type}: Attack")
                win2 = Attack(Home)
                win2.show()
                Fl.run()
                
class Attack(Home):
    
    def __init__(self, x, y, w, h, label = None):
        super().__init__(self, x, y, w, h, label)

"""
self.sl[(0,0)].activate()
self.sl[(0,0)].image(self.hitimg)
self.sl[(0,0)].deactivate()
#if (0,0) in self.sl.keys(): very cool as keys return as a list
#print("hi")
"""    


win = Home(400,400,f"Water Shoot {type}: Home")
win.show()
Fl.run()
