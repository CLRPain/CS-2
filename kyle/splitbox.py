from fltk import *

class MyApp(Fl_Window):
    def __init__(self, x,y, w, h, label=None):
        Fl_Window.__init__(self, x, y, w, h, label)
        self.color(FL_BLACK)
        self.end()

    def draw(self):
        super().draw()

        sep=10
        for y in range(0, 500, sep):
            fl_color(y//10)
            fl_line(0, y, y, 500) 
            fl_line(y, 0, 500, y) 
            fl_line(500, y, 500-y, 500) 
            fl_line(500-y, 0, 0, y) 

size=500
app = MyApp(0,0, size, size)
app.show()
Fl.run()