from fltk import *
from random import sample
from time import time

class mine(Fl_Window):
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        self.begin()
        self.ButList = [] #buttons
        self.BombList = [] #bombs
        self.BombIndex = [] #index of bombs
        self.CheckList = [] #list of checked buttons
        self.flaglist = [] #flag index
        self.start = time() #start time
        
        #makes buttons in rows of 1- then appends to self.Butlist
        for r in range(10):
            button_row = []
            for c in range(10):
                button_row.append(Fl_Button(r*50+25, c*50+25, 50, 50,))
                button_row[-1].callback(self.reveal) 
            self.ButList.append(button_row)
            
        #picks 10 random bombs and appends to self.BombList and self.BombIndex
        sample1 = sample(range(10), 10)
        sample2 = sample(range(10), 10)
        for x in range(10):
            self.BombList.append(self.ButList[sample1[x]][sample2[x]])
            #self.BombList[-1].label('bomb')
            self.BombList[-1].callback(self.reveal)
            self.BombIndex.append(self.findind(self.BombList[-1]))

        #pictures for the game
        self.flag  = Fl_PNG_Image('flag.png').copy(50, 50)
        self.bomb = Fl_JPEG_Image('bomb.jpg').copy(50, 50)
        
        self.end()
        self.resizable(self)
        
        
    def reveal(self, wid): #method to lead to other methods
        pos = self.findind(wid)
        #checks if there are 90 revealed buttons and 10 flags
        if len(set(self.CheckList)) == 90 and len(self.flaglist) <= 10: 
            self.handle_win()
            
        #checks for right clicks
        elif Fl.event_button() == FL_RIGHT_MOUSE:
            self.flag_cb(wid, pos)
                
        #if the wid is a bomb and theres no flag
        elif wid in self.BombList and wid.image() == None:
            self.handle_loss(wid)
            
        #no image or bombs so check for bombs around
        elif wid.image() == None:
            self.check(pos[0], pos[1])
            
            
    def check(self, r, c): #checks for bombs around the clicked widget
        bomb = 0
        for x in range(-1, 2):
                for y in range(-1, 2):
                    if 0<=(r+x)<10 and 0<=(c+y)<10:
                        self.CheckList.append((r, c))
                        if self.ButList[r][c].image != None:
                            self.ButList[r][c].value(1)
                        if (r+x, c+y) in self.BombIndex:
                            bomb += 1
        if bomb > 0 and self.ButList[r][c].image() == None:
            self.ButList[r][c].label(str(bomb))
            self.ButList[r][c].labelsize(50)
            return
        for x in range(-1, 2):
                for y in range(-1, 2):
                    if 0<=(r+x)<10 and 0<=(c+y)<10:
                        if (r+x, c+y) not in self.CheckList:
                            self.check(r+x, c+y)
            
    def findind(self, wid): #finds position of widget
        for x in self.ButList:
            if wid in x:
                ind = x.index(wid)
                return self.ButList.index(x), ind
            
    def flag_cb(self, wid, pos):#adds flags to widgets
        if wid.image() != None: #if theres a flag, remove it
            wid.image(None)
            wid.redraw()
            self.flaglist.remove(pos)
        elif wid.value() == 0: #no flag and not checked yet
            wid.image(self.flag)
            self.flaglist.append(pos)
    
    def handle_win(self): #win method
        timetaken = time() - self.start
        timetaken = round(timetaken, 1)
        fl_message(f'you won and it took you {timetaken} seconds')
    
    def handle_loss(self, wid): #loss method
        wid.image(self.bomb)
        for x in self.flaglist: #finds all wrong flags
            if x not in self.BombIndex:
                self.ButList[x[0]][x[1]].image(None)
                self.ButList[x[0]][x[1]].color(FL_RED)
                self.ButList[x[0]][x[1]].redraw()
                
        for x in self.BombList:
            x.image(self.bomb)
        self.redraw()
        
        for but in self.ButList:
            for wid in but:
                wid.deactivate()
        
        timetaken = round(time() - self.start, 1)
        fl_message(f'it took you {timetaken} seconds to mess up')

if __name__ == '__main__':
    win = mine(550, 550, 'Mine Sweeper')
    win.show()
    Fl.run()