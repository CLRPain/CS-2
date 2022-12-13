
from fltk import *
from random import sample

class mine(Fl_Window):
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        self.begin()
        self.ButList = []
        self.BombList = []
        self.BombIndex = []
        self.CheckList = []
        for r in range(10):
            temp = []
            for c in range(10):
                temp.append(Fl_Button(r*50, c*50, 50, 50,))
                temp[-1].callback(self.reveal) 
            self.ButList.append(temp)
            
        sel = sample(range(10), 10)
        sel2 = sample(range(10), 10)
        for x in range(10):
            self.BombList.append(self.ButList[sel[x]][sel2[x]])
            #self.BombList[-1].label('bomb')
            self.BombList[-1].callback(self.reveal)
            self.BombIndex.append(self.findind(self.BombList[-1]))

        self.flag  = Fl_PNG_Image('flag.png').copy(50, 50)
        self.bomb = Fl_JPEG_Image('bomb.jpg').copy(50, 50)
        self.end()
        self.resizable(self)
        
    def reveal(self, wid):
        pos = self.findind(wid)
        if Fl.event_button() == FL_RIGHT_MOUSE:
            if wid.image() != None:
                wid.image(None)
                wid.redraw()
            else:
                wid.image(self.flag)
        elif wid in self.BombList:
            wid.image(self.bomb)
        else:
            self.check(pos[0], pos[1])
    
    def check(self, r, c):
        bomb = 0
        for x in range(-1, 2):
                for y in range(-1, 2):
                    if 0<=(r+x)<10 and 0<=(c+y)<10:
                        self.CheckList.append((r, c))
                        self.ButList[r][c].value(1)
                        if (r+x, c+y) in self.BombIndex:
                            bomb += 1
        if bomb > 0:
            self.ButList[r][c].label(str(bomb))
            return
        for x in range(-1, 2):
                for y in range(-1, 2):
                    if 0<=(r+x)<10 and 0<=(c+y)<10:
                        if (r+x, c+y) not in self.CheckList:
                            self.check(r+x, c+y)
            
    def findind(self, wid):
        for x in self.ButList:
            if wid in x:
                ind = x.index(wid)
                return self.ButList.index(x), ind
    
    
    
    
if __name__ == '__main__':
    win = mine(500, 500, 'Mine Sweeper')
    win.show()
    Fl.run()
    #hi
