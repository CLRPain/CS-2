from fltk import *
import time

class MyApp(Fl_Window):
	def __init__(self, x, y, w, h, label=None):
		Fl_Window.__init__(self, x, y, w, h, label)
		self.color(FL_BLACK)
		self.end()
		
	def draw(self):
		
		inc=10
		
		fl_color(FL_BLUE)
		for x in range(0,self.w(),inc):
			fl_line(x,0,self.w(),x)
			fl_line(0,x,x,self.w())
			fl_line(self.w()-x,0,0,x)
			fl_line(x,self.h(),self.w(),self.h()-x)
		
			
		
			
			
size=500
app= MyApp(0,0, size, size)
app.show()
Fl.run()
