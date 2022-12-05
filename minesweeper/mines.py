from fltk import *
from random import randrange

class mine(Fl_Window):
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        self.begin()
        self.ButList = []
        self.BombList = []
        self.BombIndex = []
        for col in range(10):
            for row in range(10):
                self.ButList.append(Fl_Button(col*50, row*50, 50, 50))
                self.ButList[-1].callback(self.reveal) 
        for x in range(10):
            sel = randrange(len(self.ButList))
            self.BombList.append(self.ButList[sel])
            self.BombIndex.append(sel)
            self.ButList.pop(sel)
            self.ButList[-1].callback(self.reveal)

        self.flag  = Fl_PNG_Image('flag.png')
        self.none = Fl_PNG_Image(None)
        self.end()
        self.resizable(self)
        
        
    def reveal(self, wid):
        if Fl.event_button() == FL_RIGHT_MOUSE:
            if wid.image() == self.flag:
                pass
                #wid.image(self.none)
            else:
                wid.image(self.flag)
        elif wid in self.ButList:
            print('good')
            Fl_delete_widget(wid)
        else:
            print('bad')
    
    
if __name__ == '__main__':
    win = mine(500, 500, 'Mine Sweeper')
    win.show()
    Fl.run()
    
    
    #school