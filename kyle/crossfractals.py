from fltk import * 
class points(Fl_Window):
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        self.color(FL_BLACK)
        self.end
        self.resizable(self)
        
    def draw(self):
        super().draw()
        fl_color(FL_RED)
        P = (400, 400)
        n=12
        self.cross(P, 400, n)
        
    def cross(self, P, D, n):
        if n == 0:
            return

        D = D//2
        L = (P[0]-D, P[1]) # 200, 400
        R = (P[0]+D, P[1]) # 600, 400
        T = (P[0], P[1]-D) # 400, 200
        B = (P[0], P[1]+D) # 400, 600
        
        fl_line(L[0], L[1], R[0], R[1])
        fl_line(T[0], T[1], B[0], B[1])
        
        self.cross(L, D, n-1)
        self.cross(R, D, n-1)
        self.cross(T, D, n-1)
        self.cross(B, D, n-1)
        
        
if __name__ == '__main__':
    win = points(800, 800, '4 Points')
    win.show()
    Fl.run()
  