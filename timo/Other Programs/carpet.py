from fltk import *
import random



class fractal(Fl_Window):
	
	cc=255
	
	def __init__(self, x, y, w, h, label=None):
		Fl_Window.__init__(self, x, y, w, h, label)
		self.color(FL_BLUE)
		self.end()
		
		
	def draw(self):
		fl_color(fractal.cc)
			
		c=(0,0)
		n=5
		self.carpet(n, c, 900)
		
	def carpet(self, n, c, l):
		
		'''
		if fractal.cc==1:
			fractal.cc=255
		fractal.cc-=1
		fl_color(fractal.cc)
		'''
		
		
		if n == 0:

			return

		l=l//3
		
		
		PL=[]
		
		for row in range(3):
			for col in range(3):
				d = (c[0]+(l*row),c[1]+(l*col))
				PL.append(d)
		
		fl_rectf(PL[4][0],PL[4][1],l,l,FL_BLACK)
		
		for x in range(9):
			if x != 4:
				
				self.carpet(n-1, PL[x], l)
	
		
		





size=900
app=fractal(0,0, size, size)
app.show()
Fl.run()
