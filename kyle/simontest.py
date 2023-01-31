from fltk import *
from random import choice
from vlc import MediaPlayer

class GStart(Fl_Window):
	gsounds = ["green.mp3","red.mp3","yellow.mp3","blue.mp3"]
	gsounds2 = {"green.mp3": 0, "red.mp3": 1,"yellow.mp3": 2,"blue.mp3": 3}
	choices = []
	buts = []
	buts2 = []
	clicked = []
	N = 0
	Num = -1
	scor = 0
	high = 0
	noise = MediaPlayer()
	
	def __init__(self, w, h, name = ""):
		Fl_Window.__init__(self, w, h, name)
		self.begin()
		self.green = Fl_Button(0,0,260,260)
		self.red = Fl_Button(340,0,260,260)
		self.yellow = Fl_Button(0,340,260,260)
		self.blue = Fl_Button(340,340,260,260)
		self.sbut = Fl_Button(260,260,80,60, "Start")
		self.skor = Fl_Output(310,320,30,20, "Score:")
		self.hi = Fl_Output(310,340,30,20, "High:")
		#making objects
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
		#changing color and style
		self.sbut.tooltip("Starts game or ends current game and restarts")
		self.resizable(self)
		
		self.buts2.append(self.green)
		self.buts2.append(self.red)
		self.buts2.append(self.yellow)
		self.buts2.append(self.blue)
		
		self.sbut.callback(self.play, 1)
		self.green.callback(self.soundz, 0)
		self.red.callback(self.soundz, 1)
		self.yellow.callback(self.soundz, 2)
		self.blue.callback(self.soundz, 3)
		#adding click sounds and sequence check
		self.end()
		self.show()
	
	def play(self,w, nu):
		if nu == 1:
			self.choices.clear()
			self.buts.clear()
			self.clicked.clear()
			self.scor = 0
			self.skor.value(str(self.scor))
			#resetts game if start is clicked
		y = choice(self.gsounds)
		self.choices.append(y)
		GStart.play2(self,w)
		
	def play2(self,w):
		x = self.choices[-1]
		y = self.gsounds2.get(x)
		self.buts.append(y)
		self.buts3 = self.buts.copy() #creating a copy of sequence for checking
		for x in self.buts:
			self.but = x
			self.N += 1
			Fl.add_timeout(1.0*self.N, self.blink, x) #making sequence
		Fl.add_timeout(5.0 + 1.0*self.N, self.death)
			
	def blink(self, x):	
		self.N = 0
		GStart.noise.stop()
		GStart.noise = MediaPlayer(self.gsounds[x])
		GStart.noise.play()
		self.buts2[x].value(1) #blinking
		Fl.add_timeout(0.5, self.blink2, x)
		
	def blink2(self, x):
		self.buts2[x].value(0)
		
	def soundz(self, w, c):
		GStart.noise.stop() #button click sounds
		GStart.noise = MediaPlayer(self.gsounds[c])
		GStart.noise.play()
		self.clicked.append(c)
		Fl.remove_timeout(self.death) #removes idle counter
		
		if self.clicked[0] == self.buts3[0]:
			self.buts3.pop(0)
			self.clicked.pop(0) #if correct
		else:
			GStart.noise.stop()
			GStart.noise = MediaPlayer("error.mp3")
			GStart.noise.play()
			if self.scor > self.high:
				self.high = self.scor
				self.hi.value(str(self.scor)) #if incorrect
			
		if len(self.buts3) == 0:
			self.scor += 1
			self.skor.value(str(self.scor))
			self.skor.redraw()
			GStart.play(self,w,0)
	
	def death(self):
		self.choices.clear() #idle timer
		self.buts.clear()
		self.clicked.clear()
		self.buts3.clear()
		GStart.noise.stop()
		GStart.noise = MediaPlayer("error.mp3")
		GStart.noise.play()

win = GStart(600,600, "Simon Says")
Fl.run()