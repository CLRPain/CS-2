from fltk import *
import socket 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.settimeout(10.0)
    s.connect(('localhost', 25565))
    s.sendall('Connected to Server'.encode())
    label = 'client'
    print(s.recv(1024).decode())
    conn = s
    
except Exception as e:
    print(e)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('localhost', 25565))
    s.listen(1)
    label = 'server'
    conn, addr = s.accept()
    conn.sendall('Connected to Client'.encode())
    print(conn.recv(1024).decode())


class BattleshipSelf(Fl_Window):
    def __init__(self, x, y, width, height, label):
        Fl_Window.__init__(self, width, height, label)
        self.begin()
        self.BL = []
        XB =[]
        YB = []
        self.shiploc = []
        for col in range(10):
            for row in range(10):
                self.BL.append(Fl_Button(col*30+30,row*30+30, 30,30))
                self.BL[-1].callback(self.but_cb)
                
        for x in range(11):
            XB.append(Fl_Box(x*30,0, 30,30))
            
        for y in range(10):
            YB.append(Fl_Box(0,30+y*30, 30,30))
        self.end()
        
        for xbut in range(1, 11):
            XB[xbut].label(chr(64+xbut))
            XB[xbut].deactivate()
        XB[0].deactivate()
            
        for ybut in range(10):
            YB[ybut].label(str(ybut+1))
            YB[ybut].deactivate()
            
        self.resizable(self)

        
    def but_cb(self, wid):
        if len(self.shiploc) < 4 and wid.label() == None:
            wid.label('s')
            self.shiploc.append(self.BL.index(wid))
            print(self.shiploc)
            
            if len(self.shiploc) == 4:
                
                self.shot()
    
    def shot(self):
        conn.settimeout(None)
        if label == 'server':
            conn.send('Ready')
            data = conn.recv(1024)
            if data == 'Ready':
                    while True:
                        loc = conn.recv(1024)
                        if loc.decode() in self.shiploc:
                            self.LB[loc.decode()].label('h')
        
        else:
            data = conn.recv(1024)
            conn.send('Ready')
            if data == 'Ready':
                while True:
                    loc = conn.recv(1024)
                    if loc.decode() in self.shiploc:
                        self.LB[loc.decode()].label('h')
        
            
    
class BattleshipOther(BattleshipSelf):
    def __init__(self, x, y, width, height, label):
        super().__init__(x, y, width, height, label+' other')    

    def but_cb(self, wid):
        cord = self.BL.index(wid)
        conn.send('Ready')
        conn.send('cord'.encode())
        
        
        
if __name__ == "__main__":
    gameSelf = BattleshipSelf(0, 0, 330, 330, label)
    gameOther = BattleshipOther(330, 330, 330, 330, label)
    gameSelf.show()
    gameOther.show()
    Fl.run()
