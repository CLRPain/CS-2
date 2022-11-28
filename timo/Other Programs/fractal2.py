from fltk import *
import random


class fractal(Fl_Window):
	
	cc=255
	
	def __init__(self, x, y, w, h, label=None):
		Fl_Window.__init__(self, x, y, w, h, label)
		self.color(FL_BLACK)
		self.end()
		
		
	def draw(self):
		fl_color(fractal.cc)
			
		c=(400,400)
		n=5
		self.cross(n, 400, c)
		
	def cross(self, n, l, c):
		
		if fractal.cc==1:
			fractal.cc=255
		fractal.cc-=1
		fl_color(fractal.cc)
		
		
		n-=1
		if n == 0:

			return
			
		l=l//2
		
		L = (c[0]-l, c[1])
		R = (c[0]+l, c[1])
		T = (c[0], c[1]-l)
		B = (c[0], c[1]+l)
		
		fl_line(L[0],L[1],R[0],R[1])
		fl_line(T[0],T[1],B[0],B[1])
		
		self.cross(n, l, L)
		self.cross(n, l, R)
		self.cross(n, l, T)
		self.cross(n, l, B)


size=800
app=fractal(0,0, size, size)
app.show()
Fl.run()
