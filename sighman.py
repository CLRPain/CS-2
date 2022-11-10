from fltk import *
import random
from vlc import MediaPlayer

class GStart(Fl_Window):
	gsounds = ["green.mp3","red.mp3","yellow.mp3","blue.mp3"]
	gsounds2 = {"green.mp3": 0, "red.mp3": 1,"yellow.mp3": 2,"blue.mp3": 3}
	bsound = "error.mp3"
	choices = []
	buts = []
	buts2 = []
	clicked = []
	N = 0
	Num = -1
	def __init__(self, w, h, name = ""):
		Fl_Window.__init__(self, w, h, name)
		self.begin()
		self.green = Fl_Button(0,0,260,260)
		self.red = Fl_Button(340,0,260,260)
		self.yellow = Fl_Button(0,340,260,260)
		self.blue = Fl_Button(340,340,260,260)
		self.sbut = Fl_Button(260,260,80,60, "Start")
		self.skor = Fl_Output(310,320,30,20, "Score:")
		
		self.green.box(FL_PLASTIC_UP_BOX)
		self.red.box(FL_PLASTIC_UP_BOX)
		self.yellow.box(FL_PLASTIC_UP_BOX)
		self.blue.box(FL_PLASTIC_UP_BOX)
		
		red = fl_rgb_color(241, 54, 54)
		green = fl_rgb_color(100,215,97)
		yellow = fl_rgb_color(244, 247, 83)
		
		self.green.color(FL_GREEN)
		self.green.down_color(green)
		self.red.color(FL_RED)
		self.red.down_color(red)
		self.yellow.color(FL_YELLOW)
		self.yellow.down_color(yellow)
		self.blue.color(FL_DARK_BLUE)
		self.blue.down_color(FL_BLUE)
		
		self.sbut.tooltip("Starts game or ends current game and restarts")
		self.resizable(self)
		
		self.buts2.append(self.green)
		self.buts2.append(self.red)
		self.buts2.append(self.yellow)
		self.buts2.append(self.blue)
		
		self.sbut.callback(self.play)
		self.green.callback(self.soundz, 0)
		self.red.callback(self.soundz, 1)
		self.yellow.callback(self.soundz, 2)
		self.blue.callback(self.soundz, 3)
		self.end()
		self.show()
	
	def play(self,w):
		y = random.choice(self.gsounds)
		self.choices.append(y)
		print(self.choices)
		GStart.play2(self,w)
		
	def play2(self,w):
		
		x = self.choices[-1]
		y = self.gsounds2.get(x)
		self.buts.append(y)
		
		print(self.buts)
		for x in self.buts:
			self.but = x
			self.N += 1
			Fl.add_timeout(1.0*self.N, self.blink, x)
			
	def blink(self, x):	
		self.N = 0
		noise = MediaPlayer(self.gsounds[x])
		noise.play()
		self.buts2[x].value(1)
		Fl.add_timeout(0.5, self.blink2, x)
		
	def blink2(self, x):
		self.buts2[x].value(0)
		
	def soundz(self, w, c):
		noise = MediaPlayer(self.gsounds[c])
		noise.play()
		self.clicked.append(c)
		print(self.clicked)
		if len(self.clicked) == len(self.buts):
			for x in range(len(self.buts)):
				if self.clicked[0] == self.buts[0]:
					print(self.buts)
					self.buts.pop(0)
					self.clicked.pop(0)
				else:
					print("L")
			"""
		for x in range(len(self.buts)):
			if self.clicked[0] == self.buts[0]:
				print(self.buts)
				self.buts.pop(0)
				self.clicked.pop(0)
				"""
		"""
		y = 0
		for x in self.buts:
			if x != self.clicked[y]:
				print("bruh")
			y += 1
		self.clicked = []
		"""
		if len(self.buts) == 0:
			self.sbut.do_callback()
win = GStart(600,600, "Simon Says")
Fl.run()
