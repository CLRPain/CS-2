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
        P = (win.w()//2, win.h()//2)
        P2 = ((win.w()//2)+10, win.h()//2)
        self.dragon(P, P2)
        
    def dragon(self, P, P2):
        dir = 'R R L R R L L R R R L L R L L R R R L R R L L L R R L L R L L R R R L R R L L R R R L L R L L L R R L R R L L L R R L L R L L'
        for a in range(len(dir)):
            d = dir[a]
            x = (P2[0] - P[0])//2
            if d == 'R':
                fl_line(P[0], P[1], P2[0], P2[1]+x)
                fl_line(P2[0], P2[1]+x, P2[0]+x, P2[1])
            if d == 'L':
                fl_line(P[0], P[1], P2[0], P2[1]-x)
                fl_line(P2[0], P2[1]-x, P2[0]-x, P2[1])
        
                
        
if __name__ == '__main__':
    win = points(900, 900, '3 Points')
    win.show()
    Fl.run()
