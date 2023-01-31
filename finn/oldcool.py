
from fltk import *
#packs

def but_cb(wid):
    wid.color(FL_GREEN)

win = Fl_Window(0,0,400, 400, "Fl_Pack")
win.begin()
p=Fl_Pack(0,0, 400, 300)
p.type(Fl_Pack.HORIZONTAL)
p.begin()

bl=[]
for x in range(3):
    bl.append(Fl_Button(0, 0, p.w()//3 , 0, str(x+1)))
    bl[-1].callback(but_cb)

p.end()
p.resizable(bl[0]) # set resizable arg as either 1)widget 2)Group itself 3)None

p2= Fl_Pack(0, 300,400, 100)
p2.type(Fl_Pack.VERTICAL)
p2.begin()

b1=Fl_Button(0,0, 0, p2.h()//2,'A')
b2=Fl_Button(0,0, 0, p2.h()//2,'B')

p2.end()
p2.resizable(b1)

win.end()
win.resizable(p)
win.show()
Fl.run()
