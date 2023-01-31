from fltk import *

def but_cb(wid,x):
	if Fl.event_button() == FL_RIGHT_MOUSE:
		wid.color(FL_RED)
	elif Fl.event_button()== FL_LEFT_MOUSE:
		wid.color(FL_GREEN)
	wid.label(str(x))

LB = []

win = Fl_Window(300,400,400,400)

win.begin()
#G=Fl_Group(0,0,400,400)
#G.begin()
num = 0
for row in range(10):
	for col in range(10):
		LB.append(Fl_Button(col*40, row*40,40,40))
		LB[-1].callback(but_cb, num) #the the callback is telling but_bc to run, LB[-1], which is vv
		num += 1 #the last thing in the list, becomes the wid argument in but_cb, and num becomes x
		#the num is whats called use data in that callback line, right now its a number, but it could be anything
#G.end()
#G.resizable(None)
win.end()
win.resizable(win)
win.show()
Fl.run()

