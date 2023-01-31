from fltk import*

class cross(Fl_Window):
    x = 0
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        self.color(FL_BLACK)
        self.resizable(self)
        
    def draw(self):
        super().draw()
        fl_color(FL_BLUE)
        center = (400,400)
        k = 7
        d = 400

        self.crossy(center, d, k)
    
    def crossy(self, center, d, k):
        if k != 0:
            down = (center[0], center[1]+d)
            fl_line(down[0], down[1], center[0] , center[1] - d)
            fl_line(center[0] - d, center[1], center[0] + d, center[1])
            d = d// 2
            self.crossy(down, d, k-1)
        
    
        
        
        
win = cross(800,800,"Cool Cross")
win.show()
Fl.run()
print(cross.x)
