from fltk import*

class cross(Fl_Window):
	x = 0
	def __init__(self, w, h, label):
		Fl_Window.__init__(self, w, h, label)
		self.color(FL_BLACK)
		self.resizable(self)
		
	def draw(self):
		super().draw()
		fl_color(FL_BLUE)
		center = (400,400)
		k = 20
		d = 400

		self.crossy(center, d, k)
		
	def crossy(self, center, d, k):
		k -= 1
		cross.x += 1
		if k == 0:
			return
		d = d//2
		left = (center[0] - d, center[1])
		top = (center[0], center[1] - d)
		bottom = (center[0], center[1] + d)
		right = (center[0] + d, center[1])
		fl_line(top[0], top[1], bottom[0], bottom[1])
		fl_line(left[0], left[1], right[0], right[1])
		
		self.crossy(left, d, k)
		self.crossy(top, d, k)
		self.crossy(bottom, d, k)
		self.crossy(right, d, k)
		
	
		
		
		
win = cross(800,800,"Cool Cross")
win.show()
Fl.run()
print(cross.x)
