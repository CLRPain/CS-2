from fltk import *
import random

class tri(Fl_Window):
	
	cc=255
	
	def __init__(self, x, y, w, h, label=None):
		Fl_Window.__init__(self, x, y, w, h, label)
		self.color(FL_BLACK)
		self.end()
		
		
	def draw(self):
		fl_color(tri.cc)

			#a=(random.randrange(self.h()), random.randrange(self.h()))
			#b=(random.randrange(self.h()),random.randrange(self.h()))
			#c=(random.randrange(self.h()),random.randrange(self.h()))
		a=(350,10)
		b=(4,610)
		c=(696,610)
		n=8
		self.triangle(a,b,c,n)

		
	def mid(self, t1, t2):
		x=round((t1[0]+t2[0])/2) 
		y=round((t1[1]+t2[1])/2)
		return x, y
		
		
	def triangle(self, a,b,c,n):
		if tri.cc==1:
			tri.cc=255
		tri.cc-=1
		fl_color(tri.cc)
		
		n-=1
		if n == 0:
			return
		
		fl_line(a[0],a[1],b[0],b[1])
		fl_line(b[0],b[1],c[0],c[1])
		fl_line(c[0],c[1],a[0],a[1])
		AB=self.mid(a,b)
		AC=self.mid(a,c)
		BC=self.mid(b,c)
		
		
		self.triangle(a, AB, AC, n)
		self.triangle(b, AB, BC, n)
		self.triangle(c, AC, BC, n)
		


size=700
app=tri(0,0, size, size)
app.show()
Fl.run()

