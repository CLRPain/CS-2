from fltk import*

def but_cb(wid, x):
	if Fl.event_button() == FL_RIGHT_MOUSE:
		wid.color(FL_RED)
	elif Fl.event_button() == FL_LEFT_MOUSE:
		wid.color(FL_GREEN)
	elif Fl.event_button() == FL_MIDDLE_MOUSE:
		wid.color(FL_BLUE)
	wid.label(str(x))
	
LB = []
win = Fl_Window(300,400,400,400)

win.begin()
G = Fl_Group(0,0,400,400)
G.begin()
num=0
for col in range(24):
	for row in range(32):
		LB.append(Fl_Button(col*40,row*40,40,40))
		LB[-1].callback(but_cb, LB[num]) # the .callback is telling but_cb to run, LB[-1] is the last in the list
		num += 1
G.end()
G.resizable(None)
win.end()
win.resizable(win)
win.show()
Fl.run()
