from fltk import*

def but_cb(wid, x):
	if Fl.event_button() == FL_RIGHT_MOUSE:
		wid.color(FL_RED)
	elif Fl.event_button() == FL_LEFT_MOUSE:
		wid.color(FL_GREEN)
	#wid.label(str(x+1))
	elif Fl.event_button() == FL_MIDDLE_MOUSE:
		wid.color(FL_BLUE)
LB=[]
win = Fl_Window(300,400,400,400)

win.begin()
G=Fl_Group(0,0,400,400)#G.begin()
num=0
for col in range(128): #0, 1, 2,...
	for row in range(92):
		LB.append(Fl_Button(col*10,row*10, 10, 10))
		LB[-1].callback(but_cb, num)
		num += 1
G.end()
G.resizable(None)
win.end()
win.resizable(win)
win.show()
Fl.run()
