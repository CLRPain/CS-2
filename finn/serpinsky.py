from fltk import *

class squar(Fl_Window):
	def __init__(self, x,y, w, h, label=None):
		Fl_Window.__init__(self, x, y, w, h, label)		
		self.color(FL_DARK_BLUE)
	def draw(self):
		super().draw()
		E = win.h()
		C = (0,0)
		k = 7
		self.square(C, E, k)
		
		
	def square(self, C, E, k):
		if k == 0:
			return
		E = E // 3
		l = []
		for y in range(3):
			for x in range(3):
				l.append((C[0]+ E * x,C[1] + E * y))
		#remember counting for x in range starts at 0 so thats how you get one adn two thirds you forgot lol
		fl_rectf(l[4][0], l[4][1], E, E, FL_WHITE)
		for x in range(9):
			if x != 4:		
				self.square(l[x], E, k-1)

size=900
win = squar(0,0, size, size, "Carpet")
win.show()
Fl.run()

