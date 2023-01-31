from fltk import *

def start(w):
	Fl.add_timeout(1.0, tfunc)
	Fl.add_timeout(2.0, tfunc2)
	
def tfunc():
	Fl.repeat_timeout(1.0, tfunc)
	Square = bl[n]
	Square.color(FL_RED)
	Square.redraw()
def tfunc2():
	global n
	Fl.repeat_timeout(2.0, tfunc2)
	Square = bl[n]
	Square.color(FL_GRAY)
	Square.redraw()
	n += 1
	if n == 3:
		n = 0

x = 0
n = 0
bl = []
win = Fl_Window(500,500,300,300, "Squares")
win.begin()
Ibut1 = Fl_Button(0,0,100,100)
Ibut2 = Fl_Button(100,0,100,100)
Ibut3 = Fl_Button(200,0,100,100)
bl.append(Ibut1)
bl.append(Ibut2)
bl.append(Ibut3)
but = Fl_Button(125,150,50,50)
win.end()

but.callback(start)


win.show()
Fl.run()

#very efficient way do for x in range(len(number for butlist))
#Fl.add_timeout(2*x, function, x (list indicy))
