from fltk import *
import time

class MyApp(Fl_Window):
    def __init__(self, x,y, w, h, label=None):
        Fl_Window.__init__(self, x, y, w, h, label)
        self.color(FL_RED)
        self.end()

    def draw(self):
        Fl_Window.draw(self) #or the line below
        #super().draw() 

        sep=100
        fl_color(FL_RED) #set color before line style in Windows
        #fl_line_style(FL_DOT, 10)
        for x in range(0,self.w()+1, sep):# vertical lines
            fl_line(x,0,x,self.h())
        fl_color(FL_YELLOW)
        for y in range(0,self.h()+1, sep):# horizontal lines
            fl_line(0,y,self.w(),y)

size=601
app = MyApp(0,0, size, size)
app.show()
Fl.run()
