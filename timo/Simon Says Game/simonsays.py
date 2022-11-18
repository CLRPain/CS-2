from fltk import *
import vlc
import random



class Simon(Fl_Window):
	
	'''
	d='/home/inter/simon_audio/'
	sounds=[str(d + 'green.mp3'),
			str(d + 'red.mp3'),
			str(d + 'blue.mp3'),
			str(d + 'yellow.mp3'),
			str(d + 'error.mp3'),
				]
	'''
	sounds=['green.mp3',
			'red.mp3',
			'blue.mp3',
			'yellow.mp3',
			'error.mp3'
			]
	
		
	high=''
	Cscore=''
	Buts=[]
	gameseq=[]	
	sequence=[]
	score=0
	a=0
	cursound=vlc.MediaPlayer()
	
	def __init__(self, w, h, label):
		
		Fl_Window.__init__(self, w, h, label)
		self.begin()
			
		# Buttons and outputs
		green = Fl_Button(100,100,200,200)
		red = Fl_Button(400,100,200,200)
		blue = Fl_Button(400,400,200,200)
		yellow = Fl_Button(100,400,200,200)
		
		self.start = Fl_Button(325,280,50,50,'Start')
		Simon.high = Fl_Output(400,365,50,25)
		Simon.cscore = Fl_Output(250,365,50,25)
		
		# Colors and labels
		green.color(FL_DARK_GREEN)
		green.down_color(FL_GREEN)
		red.color(FL_DARK_RED)
		red.down_color(FL_RED)
		blue.color(FL_DARK_BLUE)
		blue.down_color(FL_BLUE)
		yellow.color(FL_DARK_YELLOW)
		yellow.down_color(FL_YELLOW)
		
		self.start.color(FL_CYAN)
		Simon.high.label('Highscore: ')
		Simon.high.align(FL_ALIGN_TOP)
		Simon.high.value('0')
		Simon.cscore.label('Score: ')
		Simon.cscore.align(FL_ALIGN_TOP)
		Simon.cscore.value('0')
		
		# Adding to the list "Buts"
		Simon.Buts.append(green)
		Simon.Buts.append(red)
		Simon.Buts.append(yellow)
		Simon.Buts.append(blue)
		
		# Box types
		for x in range(4):
			Simon.Buts[x].box(FL_PLASTIC_UP_BOX)
			Simon.Buts[x].callback(self.playgame_cb, x)
		
		self.start.callback(self.play_cb)
		
		self.end()
		self.resizable(self)
		Simon.butdisable()
		
		
# When a mistake is made during a game:
	def gameover():
		Fl.remove_timeout(Simon.gameover)
		Simon.cscore.value('0')
		Simon.cursound=vlc.MediaPlayer(Simon.sounds[4])
		Simon.cursound.play()
		fl_message(f'Game Over! Your score is {Simon.score}')
		Simon.sequence.clear()
		if Simon.Buts[0].active() == True:
			Simon.butdisable()
		if int(Simon.score) > int(Simon.high.value()): # Changing highscore
			Simon.high.value(str(Simon.score))


# Makes the buttons blink
	def blink(n):
		if Simon.Buts[n].value() == 0: 
			Simon.Buts[n].value(1)
			return
		
		Simon.Buts[n].value(0)
		
				
# Sounds for when playing the current sequence, time-outs are made in "playseq"
	def playsounds(n):
		Simon.cursound.stop()
		Simon.cursound=vlc.MediaPlayer(Simon.sounds[Simon.sequence[n]])
		Simon.cursound.play()
		Simon.blink(Simon.sequence[n]) # Blink the buttons
		Fl.add_timeout(0.5, Simon.blink, Simon.sequence[n])



# Sounds for when player clicks button, called from "playgame_cb"
	def sound(n):
		Simon.cursound.stop()
		Simon.cursound=vlc.MediaPlayer(Simon.sounds[n])
		Simon.cursound.play()

		
# Creating and playing the sequence of buttons
	def playseq(self):
		Fl.remove_timeout(Simon.gameover)
		Simon.cscore.value(str(Simon.score))
		if Simon.Buts[0].active() == True:
			Simon.butdisable()
		x=random.randrange(4) # Randomizer to choose button
		Simon.sequence.append(x)
		for n in range(len(Simon.sequence)):
			Fl.add_timeout(1.0*n, Simon.playsounds, n) # Time outs for each sound
		Fl.add_timeout(len(Simon.sequence)+0.5, Simon.playgame_cb, -1) # Time out for after the sounds are done


# "Start" Button callback
	def play_cb(self, w):
		Fl.remove_timeout(Simon.playsounds)
		Fl.remove_timeout(Simon.playgame_cb)
		Fl.remove_timeout(Simon.gameover)
		Simon.gameseq.clear()
		Simon.sequence.clear()
		Simon.score=0
		Simon.playseq(self)
		self.cscore.value('0')

	
# When its the players turn
	def playgame_cb(self, w=-1, n=-1):
		if w == -1: # If the function is called from the code
			Simon.a=0
			if Simon.Buts[0].active() == False:
				Simon.butdisable()
			Simon.score+=1
			Fl.add_timeout(5, Simon.gameover)
			return
		Fl.remove_timeout(Simon.gameover)
		Fl.add_timeout(5, Simon.gameover)
		Simon.sound(n) # If the function is called from a callback
		Simon.gameseq.append(n)
		Simon.a+=1
		if len(Simon.gameseq) > len(Simon.sequence): #Incase the player uses an autoclicker and tries to crash the program
			Simon.gameover()
		if len(Simon.gameseq) < int(1+len(Simon.sequence)): # Check if its the right button
			if Simon.gameseq[int(Simon.a-1)] != Simon.sequence[int(Simon.a-1)]:
				Simon.gameover()
			if len(Simon.gameseq) == len(Simon.sequence):
				Simon.gameseq.clear()
				Fl.add_timeout(1, Simon.playseq, self)
			return
				

# Enable/Disable the color buttons
	def butdisable():
		if Simon.Buts[0].active() == True: # If Buttons are enabled
			for x in range(len(Simon.Buts)):
				Simon.Buts[x].deactivate()
				Simon.Buts[x].redraw()
			return
		for x in range(len(Simon.Buts)): # If Buttons are disbabled
			Simon.Buts[x].activate()
			Simon.Buts[x].redraw()
		return

# Starts the program:
if __name__ == '__main__':
	Fl.scheme('plastic')
	game = Simon(700, 700, 'Simon Says')
	game.show()
	Fl.run()
