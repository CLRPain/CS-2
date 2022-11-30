from fltk import *
#allowed to die on first click
class Mines(Fl_Window):
	def __init__(self, w, h, label = None):
		Fl_Window.__init__(self, w, h, label)
		
		
		
		
		
		
		
		
win = Mines(400, 400, "Mynes")
win.show()
Fl.run()
