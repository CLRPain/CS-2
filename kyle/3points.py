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
        self.triangle(A, B, C, 6)
        
    def triangle(self, A, B, C, n):
        n -= 1
        print('hi')
        if n == 0:
            return 
        fl_line(A[0], A[1], B[0], B[1])
        fl_line(A[0], A[1], C[0], C[1])
        fl_line(B[0], B[1], C[0], C[1])
        nA = self.mid(A, B)
        nB = self.mid(A, C)
        nC = self.mid(B, C)
        
        self.triangle(nA, nB, nC, n)
        
    def mid(self, start, end):
        midx = (start[0] + end[0])//2
        midy = (start[1] + end[1])//2
        return midx, midy
        
if __name__ == '__main__':
    win = points(700, 700, '3 Points')
    win.show()
    Fl.run()