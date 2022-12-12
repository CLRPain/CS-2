from fltk import *
import random
#allowed to die on first click
class Mines(Fl_Window):
    L = []
    BL = []
    Flags = 10
    b = 0
    def __init__(self, w, h, label = None):
        Fl_Window.__init__(self, w, h, label)       
        for r in range(10):
            temp = [] 
            for c in range(10):
                temp.append(Fl_Button((c*50)+ 20, (r *50) + 60, 50,50))
                temp[c].callback(self.notboom)
            self.L.append(temp)
        o = random.sample(range(10), 10)
        t = random.sample(range(10), 10)
        for x in range(10):
            self.BL.append(self.L[o[x]][t[x]])
        for but in self.BL:
            but.callback(self.boom)
            but.label("bomb")

            
                        

                
        
    def notboom(self, wid):
        #wid.hide()
        for but in self.L:
            if wid in but:
                found2 = but.index(wid)
                found = self.L.index(but)
                print(found, found2)
        rounds = 0
        #TO DO: MAKE THE EMPTY SQUARES ALL DISSAPEAR IF CONNECTED TO EACH OTHER will be easier if we can move this to __init__
        for x in range(-1,2):
            for y in range(-1,2):
                if 0<=(found+x) < 10 and 0<=(found2+y)<10:
                    if self.L[found + x][found2 + y] in self.BL:
                        rounds += 1
        round = str(rounds)
        wid.label(round)
                    
                    
        #self.L[0][1].hide() use stuff like this very helpful because coords
    """
    def around(self, r, c):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if 0<=(r+x) < 5 and 0<=(c+y)<5:
                    pass
                    #print([self.L[r+x][c+y]])
    """
    def boom(self, w):
        if Fl.event_button() == FL_LEFT_MOUSE and self.b == 0:
            img = Fl_JPEG_Image("bomb.jpg")
            img = img.copy(50,50)
            w.image(img)
            
        if Fl.event_button() == FL_RIGHT_MOUSE:
            if w.image() == None:
                img = Fl_PNG_Image("flag.png")
                img = img.copy(50,50)
                w.image(img)
                self.b = 1
                
            else:
                w.image(None)
                self.b = 0
                
    """
    def notboom(self,w):
        if Fl.event_button() == FL_LEFT_MOUSE:
            w.hide()
            p = self.cl.index(w) - 11
            pb = self.cl[p]
            if pb not in self.minel:
                pb.hide()
            if pb in self.minel:
                pb.label("hi") #change this lel
        if Fl.event_button() == FL_RIGHT_MOUSE:
            if self.Flags > 0:
                if w.image() == None:	
                    img = Fl_PNG_Image("flag.png")
                    img = img.copy(50,50)
                    w.image(img)
                    #self.Flags -= 1
                elif w.image() != None:
                    w.image(None)
                    w.redraw()
                #	self.Flags += 1
"""
                    


        
        
        
        
win = Mines(540, 580, "Mynes")
win.show()
Fl.run()
