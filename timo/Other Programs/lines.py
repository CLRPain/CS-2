from fltk import *
import time

class MyApp(Fl_Window):
	def __init__(self, x, y, w, h, label=None):
		Fl_Window.__init__(self, x, y, w, h, label)
		self.color(FL_BLACK)
		self.end()
	
	def draw(self):
		sep=100 # Change this number, lower number = more lines
		fl_color(FL_RED)
		
		for x in range(0,self.w()+1, sep):
			fl_line(x,0,x,self.h())
		fl_color(FL_YELLOW)
		for y in range(0,self.h()+1, sep):
			fl_line(0,y,self.w(),y)
		
		fl_pie(300,300, 100, 100, 0, 360)
		
size=601
app= MyApp(0,0, size, size)
app.show()
Fl.run()
