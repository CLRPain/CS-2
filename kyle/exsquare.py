from fltk import *

class Carpet(Fl_Double_Window):
    def __init__(self, level):
        super().__init__(729, 729,'Sierpinski Carpet') #3**6=729
        self.level=level
        self.color(FL_BLUE)

    def draw(self):
        super().draw()
        fl_color(FL_WHITE)
        self.pattern(self.level, (0,0), self.w())

    def pattern(self, n, loc, w):
        if n>0:
            w = round(w/3)
            fl_rectf(loc[0]+w, loc[1]+w, w, w)
            locations=[]
            for c in range(3):
                for r in range(3):
                    locations.append( (loc[0]+(r*w), loc[1]+(c*w)) )
            locations.pop(4) #do not recurse center square
            for point in locations:
                self.pattern(n-1, point, w)
app=Carpet(6)
app.show()
Fl.run()
