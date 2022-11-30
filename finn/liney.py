from fltk import *
import time

class MyApp(Fl_Window):
	def __init__(self, x,y, w, h, label=None):
		Fl_Window.__init__(self, x, y, w, h, label)		

	def draw(self):
		super().draw()
		fl_color(FL_RED)
		T1 = (350,10)
		T2 = (4, 610)
		T3 = (696,610)
		k = 12
		self.triangle(T1, T2, T3, k)
		
	def triangle(self, T1, T2, T3, k):
		k -= 1
		if k == 0:
			return
		fl_line(T1[0], T1[1], T2[0], T2[1])
		fl_line(T2[0], T2[1], T3[0], T3[1])
		fl_line(T1[0], T1[1], T3[0], T3[1])
		mid1 = self.middle(T1, T2)
		mid2 = self.middle(T1, T3)
		mid3 = self.middle(T2, T3)
		self.triangle(T1, mid1, mid2, k)
		self.triangle(T2, mid1, mid3, k)
		self.triangle(T3, mid2, mid3, k)

	def middle(self, T1, T2):
		O1 = (T1[0] + T2[0]) //2 
		O2 = (T1[1] + T2[1]) //2 
		return O1, O2 

size=700
app = MyApp(0,0, size, size)
app.show()
Fl.run()
