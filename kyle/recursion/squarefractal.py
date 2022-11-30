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
        self.carpet(D, P, 16)
        
    def carpet(self, D, P, n):
        if n == 0:
            return 
        D = D//3
        d1 = P[0]+D, P[1]+D
        d2 = P[0]+D, P[1]+D
        fl_rectf(d1[0], d1[1], d2[0], d2[1], FL_WHITE)
        self.carpet(D, d1, n-1)
        
if __name__ == '__main__':
    win = points(700, 700, '3 Points')
    win.show()
    Fl.run()