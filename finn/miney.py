from fltk import *
import random
#allowed to die on first click
class Mines(Fl_Window):
	butl = []
	minel = []
	cl = []
	Flags = 10
	def __init__(self, w, h, label = None):
		Fl_Window.__init__(self, w, h, label)
		for row in range(10):
			for col in range(10):
				but = Fl_Button((col*50)+ 20, (row*50) + 60, 50,50)
				self.butl.append(but)
				self.cl = self.butl.copy()
		for x in range(10):
			choice = random.choice(self.butl)
			self.minel.append(choice)
			dead = self.butl.index(choice)
			self.butl.pop(dead)
		for mine in self.minel:
			mine.callback(self.boom)
		for but in self.butl:
			but.callback(self.notboom)
			
	def boom(self, w):
		if Fl.event_button() == FL_LEFT_MOUSE:
			img = Fl_JPEG_Image("bomb.jpg")
			img = img.copy(50,50)
			w.image(img)
		if Fl.event_button() == FL_RIGHT_MOUSE:
			img = Fl_PNG_Image("flag.png")
			img = img.copy(50,50)
			w.image(img)
	def notboom(self,w):
		if Fl.event_button() == FL_LEFT_MOUSE:
			w.hide()
			p = self.cl.index(w) - 11
			pb = self.cl[p]
			if pb not in self.minel:
				pb.hide()
			if pb in self.minel:
				pb.label("hi") #change this lel
		if Fl.event_button() == FL_RIGHT_MOUSE:
			if self.Flags > 0:
				if w.image() == None:	
					img = Fl_PNG_Image("flag.png")
					img = img.copy(50,50)
					w.image(img)
					#self.Flags -= 1
				elif w.image() != None:
					w.image(None)
					w.redraw()
				#	self.Flags += 1

					


		
		
		
		
win = Mines(540, 580, "Mynes")
win.show()
Fl.run()
