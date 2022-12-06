from fltk import *
from random import randrange

class mine(Fl_Window):
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        self.begin()
        self.ButList = []
        self.BombList = []
        for r in range(10):
            temp = []
            for c in range(10):
                temp.append(Fl_Button(r*50, c*50, 50, 50,))
                temp[-1].callback(self.reveal) 
            self.ButList.append(temp)
            
        for x in range(10):
            sel = randrange(10) 
            sel2 = randrange(10) 
            self.BombList.append(self.ButList[sel][sel])
            self.BombList[-1].callback(self.reveal)

        self.flag  = Fl_PNG_Image('flag.png').copy(50, 50)
        self.end()
        self.resizable(self)
        
        
        
    def reveal(self, wid):
        wid.hide()
        return
        if Fl.event_button() == FL_RIGHT_MOUSE:
            if wid.image() != None:
                wid.image(None)
                wid.redraw()
            else:
                wid.image(self.flag)
        elif wid in self.BombList:
            print('bad')
        else:
            self.ButList.index(wid)
            print('good')
            wid.hide()
    
    def check(self, wid):
        print(self.ButList.index(wid))
    
    
    
    
if __name__ == '__main__':
    win = mine(500, 500, 'Mine Sweeper')
    win.show()
    Fl.run()