from fltk import *
import random
import time
class Mines(Fl_Window):
    L = [] #lists for all buts, bomb buts, and recursion
    BL = []
    CL = []
    CL2 = []
    def __init__(self, w, h, label = None):
        Fl_Window.__init__(self, w, h, label)
        
        for r in range(10):
            temp = [] 
            for c in range(10): #making buts
                temp.append(Fl_Button((c*50)+ 20, (r *50) + 20, 50,50))
                temp[c].callback(self.notboom)
            self.L.append(temp)
            
        o = random.sample(range(10), 10) #finding bombs
        t = random.sample(range(10), 10)
        for x in range(10):
            self.BL.append(self.L[o[x]][t[x]])
            self.BL[-1].callback(self.boom)
            
        self.tim = time.time()
        self.resizable(self)    
        
        self.img = Fl_JPEG_Image("bomb.jpg").copy(50,50)
        self.img2 = Fl_PNG_Image("flag.png").copy(50,50)
        
    def notboom(self, wid):
        if wid not in self.CL2:
            self.CL2.append(wid)
            
        if Fl.event_button() == FL_LEFT_MOUSE and wid.image() == None:
            for but in self.L:
                if wid in but:
                    found2 = but.index(wid) #finding coordinates
                    found = self.L.index(but)
                    print(found, found2)
                    
            rounds = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0<=(found+x) < 10 and 0<=(found2+y)<10:
                        if self.L[found + x][found2 + y] in self.BL:
                            rounds += 1 #counting surrounding bombs
            roundz = str(rounds)
            wid.value(1)
            
            if rounds == 0:
                if wid not in self.CL: #recursing and revealing blank buts
                    self.CL.append(wid)
                    for x in range(-1,2):
                        for y in range(-1,2):
                            if 0<=(found+x) < 10 and 0<=(found2+y)<10:
                                self.L[found + x][found2 + y].do_callback()    
            else:
                wid.label(roundz)
            
        if Fl.event_button() == FL_RIGHT_MOUSE:
            if wid.image() == None:
                if wid.value() == 0: #placing flags
                    wid.image(self.img2)  
            else:
                wid.image(None)
                
        if len(set(self.CL2)) == 90:
            tt = round(time.time() - self.tim, 1)
            fl_message(f"You Won In {tt} Seconds!")
                    
    def boom(self, w):
        if Fl.event_button() == FL_LEFT_MOUSE and w.image() == None:
            w.image(self.img)
            for but in self.BL:
                but.image(self.img)
            for list in self.L:
                for but in list:
                    if but.image() != None and but not in self.BL:
                        but.image(None)
                        but.color(FL_RED) #displaying incorrect flags on loss
                        but.label("Wrong")
                        
            tt = time.time() - self.tim
            tt = round(tt, 1)
            
            for list in self.L:
                for but in list:
                    but.deactivate()
                    
            fl_message(f"Sorry you lose. \nTime Taken: {tt} seconds")
                
        if Fl.event_button() == FL_RIGHT_MOUSE:
            if w.image() == None:
                w.image(self.img2) #placing flags
            else:
                w.image(None)
                
win = Mines(540, 540, "Mynes")
win.show()
Fl.run()
