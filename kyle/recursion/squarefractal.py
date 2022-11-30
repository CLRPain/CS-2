from fltk import * 
class points(Fl_Window):
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        self.color(FL_BLUE)
        self.end
        self.resizable(self)
        
    def draw(self):
        super().draw()
        fl_color(FL_RED)
        D = win.w()
        P = (0, 0)
        self.carpet(D, P, 6)
        
    def carpet(self, D, P, n):
        if n == 0:
            return 
        D = D//3
        pointlist = []
        for row in range(3):
            for col in range(3):
                point = P[0]+(D*row), P[1]+(D*col)
                pointlist.append(point)
                
        fl_rectf(pointlist[4][0], pointlist[4][1], D, D, FL_WHITE)
        for x in range(9):
            if x != 4:
                self.carpet(D, pointlist[x], n-1)
        
if __name__ == '__main__':
    win = points(900, 900, '3 Points')
    win.show()
    Fl.run()
