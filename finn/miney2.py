from fltk import *
import random
import time
class Mines(Fl_Window):
    L = []
    BL = []
    CL = []
    CL2 = []
    Flags = 10
    b = 0
    b2 = 0
    def __init__(self, w, h, label = None):
        Fl_Window.__init__(self, w, h, label)
        for r in range(10):
            temp = [] 
            for c in range(10):
                temp.append(Fl_Button((c*50)+ 20, (r *50) + 20, 50,50))
                temp[c].callback(self.notboom)
            self.L.append(temp)
        o = random.sample(range(10), 10)
        t = random.sample(range(10), 10)
        for x in range(10):
            self.BL.append(self.L[o[x]][t[x]])
        for but in self.BL:
            but.callback(self.boom)
        self.tim = time.time()
        self.resizable(self)    
        
    def notboom(self, wid):
        if wid not in self.CL2:
            self.CL2.append(wid)
        if Fl.event_button() == FL_LEFT_MOUSE and self.b2 == 0:
            for but in self.L:
                if wid in but:
                    found2 = but.index(wid)
                    found = self.L.index(but)
                    print(found, found2)
            rounds = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if 0<=(found+x) < 10 and 0<=(found2+y)<10:
                        if self.L[found + x][found2 + y] in self.BL:
                            rounds += 1
            round = str(rounds)
            wid.value(1)
            if rounds == 0:
                if wid not in self.CL:
                    self.CL.append(wid)
                    for x in range(-1,2):
                        for y in range(-1,2):
                            if 0<=(found+x) < 10 and 0<=(found2+y)<10:
                                self.L[found + x][found2 + y].do_callback()    
            else:
                wid.label(round)
        if Fl.event_button() == FL_RIGHT_MOUSE:
            if wid.image() == None:
                if wid.value() == 0:
                    img = Fl_PNG_Image("flag.png")
                    img = img.copy(50,50)
                    wid.image(img)
                    self.b2 = 1
                
            else:
                wid.image(None)
                self.b2 = 0
                
        if len(set(self.CL2)) == 90:
            fl_message("You Win!")
                    
    def boom(self, w):
        if Fl.event_button() == FL_LEFT_MOUSE and self.b == 0:
            img = Fl_JPEG_Image("bomb.jpg")
            img = img.copy(50,50)
            w.image(img)
            for but in self.BL:
                img = Fl_JPEG_Image("bomb.jpg")
                img = img.copy(50,50)
                but.image(img)
                but.redraw()
            for list in self.L:
                for but in list:
                    if but.image() != None and but not in self.BL:
                        but.image(None)
                        but.color(FL_RED)
                        but.label("Wrong")
                        but.redraw()
            tt = time.time() - self.tim
            tt = round(tt, 1)
            for list in self.L:
                for but in list:
                    but.deactivate()
            fl_message(f"Sorry you lose, \nTime Taken: {tt} seconds")
                
            
        if Fl.event_button() == FL_RIGHT_MOUSE:
            if w.image() == None:
                img = Fl_PNG_Image("flag.png")
                img = img.copy(50,50)
                w.image(img)
                self.b = 1
                
            else:
                w.image(None)
                self.b = 0

win = Mines(540, 540, "Mynes")
win.show()
Fl.run()
