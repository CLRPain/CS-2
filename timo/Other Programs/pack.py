'''
from fltk import *

w = Fl_Window(500,100,300,400, "Pack Demo")
w.begin()

p1 = Fl_Pack(0,0,300,400)
p1.begin()
but1 = Fl_Button(0,0,0,50)
but2 = Fl_Button(0,0,0,50)
but3 = Fl_Button(0,0,0,50)
p1.end()

p1.type(FL_VERTICAL)
p1.spacing(25)

w.end()

Fl.scheme("gtk+")
w.show()
Fl.run()
'''
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
win.resizable(win)
win.show()
Fl.run()
