from fltk import *
import time

class MyApp(Fl_Window):
    def __init__(self, x,y, w, h, label=None):
        Fl_Window.__init__(self, x, y, w, h, label)
        self.color(FL_BLACK)
        self.end()

    def draw(self):
        Fl_Window.draw(self) 
        
        rad = 601
        y = 0
        for x in range(601):        
            for col in range(1):
                fl_color(col)
                fl_pie(y, y, rad , rad , 0, 360)
                y += 1
                rad -= 2

size=601
app = MyApp(0,0, size, size)
app.show()
Fl.run()