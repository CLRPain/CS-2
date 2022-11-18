from fltk import *

def but_cb(wid):
	print('event')
	
win = Fl_Window(0,0,400,400, "Shortcuts")
win.begin()
but = Fl_Button(10,10,170,50,"OK")
win.end()
but.shortcut(ord('6'))

but.callback(but_cb)

# but.shortcut(FL_CRTL | ord('a'))

win.show()
Fl.run()
