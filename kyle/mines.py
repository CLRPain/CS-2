from fltk import *
from random import randrange

class mine(Fl_Window):
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        self.begin()
        self.ButList = []
        self.BombList = []
        self.BombIndex = []
        a = 0
        for col in range(10):
            for row in range(10):
                self.ButList.append(Fl_Button(col*50, row*50, 50, 50, str(a)))
                self.ButList[-1].callback(self.reveal) 
                a += 1
        for x in range(10):
            sel = randrange(len(self.ButList))
            self.BombList.append(self.ButList[sel])
            self.BombIndex.append(sel)
            #self.ButList.pop(sel)
            self.ButList[-1].callback(self.reveal)

        self.flag  = Fl_PNG_Image('flag.png').copy(50, 50)
        self.end()
        self.resizable(self)
        
        
    def reveal(self, wid):
        self.check(wid)
        if Fl.event_button() == FL_RIGHT_MOUSE:
            if wid.image() != None:
                wid.image(None)
                wid.redraw()
            else:
                wid.image(self.flag)
        elif wid in self.ButList:
            print('good')
            wid.hide()
            
        else:
            print('bad')
    
    def check(self, wid):
        if wid not in self.BombList:
            num = self.ButList.index(wid)
            TopL = num - 11
            L = num - 10
            DownL = num - 9 
            print(num, TopL, L, DownL)
    
    
    
    
if __name__ == '__main__':
    win = mine(500, 500, 'Mine Sweeper')
    win.show()
    Fl.run()