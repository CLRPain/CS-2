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
        A = (350, 10)
        B = (4, 610)
        C = (696, 610)
        self.triangle(A, B, C, 2)
        
    def triangle(self, A, B, C, n):
        if n == 0:
            return 
        n -= 1
        fl_line(A[0], A[1], B[0], B[1])
        fl_line(A[0], A[1], C[0], C[1])
        fl_line(B[0], B[1], C[0], C[1])
        AB = self.mid(A, B)
        AC = self.mid(A, C)
        BC = self.mid(B, C)
        
        self.triangle(A, AB, AC, n)
        self.triangle(B, AB, BC, n)
        self.triangle(C, AC, BC, n)
        #self.triangle(AB, AC, BC, n)
        
    def mid(self, start, end):
        midx = (start[0] + end[0])//2
        midy = (start[1] + end[1])//2
        return midx, midy
        
if __name__ == '__main__':
    win = points(700, 700, '3 Points')
    win.show()
    Fl.run()