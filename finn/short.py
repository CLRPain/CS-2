from fltk import *

def but_cb(wid):
	print("event happened")
	
win = Fl_Window(0,0,400,400, "shortcuts")
win.begin()
but = Fl_Button(10,10,170,50,"OK")
win.end()

but.shortcut(ord('6'))


but.callback(but_cb)

win.show()
Fl.run()
