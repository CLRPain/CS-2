from fltk import *
class sequence(Fl_Window):
    def __init__(self, xaxis, yaxis, 
                 width, height, label='sequence flasher'):
        Fl_Window.__init__(self, xaxis, yaxis, width, height, label)
        self.begin()
        self.b = []
        self.x = 0
        for col in range(3):
            button = Fl_Button(col*100, 90, 100, 100)
            self.b.append(button)
            
        but = Fl_Button(125, 300, 50, 50, "click")
        self.end()
        but.callback(self.but_cb)

        self.show()
        
    def but_cb(self, w):
        Fl.add_timeout(1.0, self.sqclr)
    
    def sqclr(self):
        if self.x == len(self.b):
            self.x = 0
        if self.b[self.x].color() == FL_GRAY:
            self.b[self.x].color(FL_RED)
            self.b[self.x].redraw()
        else:
            self.b[self.x].color(FL_GRAY)
            self.b[self.x].redraw()
            self.x += 1
        Fl.repeat_timeout(1.0, self.sqclr)
    
win = sequence(500, 100, 300, 400, "my gui")
Fl.run()




'''
from fltk import *

def but_cb(w):
    Fl.add_timeout(1.0, sqclr)
    
def sqclr():
    global x
    if x == len(b):
        x = 0
    if b[x].color() == FL_GRAY:
        b[x].color(FL_RED)
        b[x].redraw()
    else:
        b[x].color(FL_GRAY)
        b[x].redraw()
        x += 1
    Fl.repeat_timeout(1.0, sqclr)

win = Fl_Window(500, 100, 300, 400, "my gui")
win.begin()
b = []
x = 0
for col in range(3):
    button = Fl_Button(col*100, 90, 100, 100)
    b.append(button)
    
but = Fl_Button(125, 300, 50, 50, "click")
win.end()
but.callback(but_cb)

win.show()
Fl.run()
'''