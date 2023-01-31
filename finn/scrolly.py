from fltk import *
#scroll

def but_cb(wid):
    wid.color(FL_GREEN)

win = Fl_Window(0,0,400, 400, "Fl_Scroll")
win.begin()

s=Fl_Scroll(0,0, 400, 300)
s.type(Fl_Scroll.HORIZONTAL)
s.begin()

bl=[]
for x in range(19):
    #bl.append(Fl_Button(x*40, 0, 40 , 280, str(x+1)))
    bl.append(Fl_Button(x*40, 0, 40 , s.h(), str(x+1)))
    bl[-1].callback(but_cb)

s.end()
s.resizable(s)

s2= Fl_Scroll(0, 300,400, 100)
s2.begin()

sl=[]
for x in range(20):
    sl.append(Fl_Button(0, x*30+300, 380 , 30, str(x+1)))
    sl[-1].callback(but_cb)

s2.end()
s2.resizable(s2)
s2.type(Fl_Scroll.VERTICAL)

win.end()
win.resizable(win)
win.show()
Fl.run()
