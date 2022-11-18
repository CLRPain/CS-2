from fltk import *
import time

class MyApp(Fl_Window):
	def __init__(self, x, y, w, h, label=None):
		Fl_Window.__init__(self, x, y, w, h, label)
		self.color(FL_BLACK)
		self.end()
		
		
		
	def draw(self):
			
		num=32
		color=(256)
		circle=720
		cc=0
		
		for x in range(256):
			fl_color(color)
			fl_pie(cc,cc,circle ,circle, 0, 360)
			circle=circle-num
			cc=cc+int(num/2)
			color=color-1

			
size=750
app= MyApp(0,0, size, size)
app.show()
Fl.run()
