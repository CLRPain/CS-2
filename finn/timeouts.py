from fltk import *
"""
def tofunc():
        but.do_callback()
        Fl.repeat_timeout(1.0, tofunc)

def but_cb(w):
        if but.image()!=None:
                print("remove image")
                but.image(None)
                but.redraw()
        else:
                print("put image")
                but.image(pic)
                but.redraw()

def but2_cb(w):
        Fl.remove_timeout(tofunc)

win = Fl_Window(500,100,300,400,"my gui")
win.begin()
but = Fl_Button(100,90, 100, 110)
but2= Fl_Button(100,250,70,30,"Stop")
win.end()

but.callback(but_cb)
but2.callback(but2_cb)
pic=(Fl_PNG_Image("bruhgrams.png")).copy(but.w(),but.h())
Fl.add_timeout(1.0, tofunc)

win.show()
Fl.run()
"""

def dothis(v):
	print(v)
	but.do_callback()
	#Fl.repeat_timeout(1.0, dothis)
	
def but_cb(w):
	Fl.remove_timeout(dothis)
	
win = Fl_Window(500,100,300,400,"my gui")
win.begin()
but = Fl_Button(100,90,100,110)
win.end()

but.callback(but_cb)

Fl.add_timeout(3.0, dothis, 1)
Fl.add_timeout(4.0, dothis, 2)
Fl.add_timeout(5.0, dothis, 3)
win.show()
Fl.run()
