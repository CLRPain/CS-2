from fltk import *
from random import randrange
from vlc import MediaPlayer

class simon(Fl_Window):
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        self.begin()
        self.buttons = []
        self.sounds = ['red.mp3', 'blue.mp3', 'green.mp3', 'yellow.mp3']
        self.effects = MediaPlayer()
        self.sequence = []
        
        red = Fl_Button(0, 0, 200, 200, '0')#up left
        blue = Fl_Button(self.w()-200, 0, 200, 200, '1')#up right
        green = Fl_Button(0, self.h()-200, 200, 200, '2')#down left
        yellow = Fl_Button(self.w()-200, self.h()-200, 200 ,200, '3')#down right
        self.startbut = Fl_Button(self.w()//2-40, self.h()//2-40 ,80 ,80, "Start")
        self.current = Fl_Output(self.w()//2-40, 350 ,80 ,30, 'Current') #current score
        self.best = Fl_Output(self.w()//2-40, 390 ,80 ,30, "Best") #highscore
        self.current.value('0')
        self.best.value('0')
        
        red.color(FL_DARK_RED)
        blue.color(FL_DARK_BLUE)
        green.color(FL_DARK_GREEN)
        yellow.color(FL_DARK_YELLOW)
        
        red.down_color(FL_RED)
        blue.down_color(FL_BLUE)
        green.down_color(FL_GREEN)
        yellow.down_color(FL_YELLOW)
        
        self.end()
        self.resizable(self)
        
        self.buttons.append(red)
        self.buttons.append(blue)
        self.buttons.append(green)
        self.buttons.append(yellow)
        
        self.buttons[0].callback(self.game, 0)
        self.buttons[1].callback(self.game, 1)
        self.buttons[2].callback(self.game, 2)
        self.buttons[3].callback(self.game, 3)

        self.startbut.callback(self.start)
    
    def sound(self, num): #play sound effects for button presses
        self.effects.stop()
        self.effects = MediaPlayer(self.sounds[num])
        self.effects.play()
            
    def start(self, w): #start the game/reset
        if len(self.sequence) > 0:
            self.sequence.clear()
            self.current.value('0')
        self.score = 0
        Fl.add_timeout(0.5, self.seq)
        
    def seq(self): #make a list of button sequences
        self.times = 1
        seqint = randrange(0, 4)
        self.sequence.append(seqint)
        if len(self.sequence) > self.score:
            self.sequence2 = self.sequence.copy() #make copies to change later
            self.sequence3 = self.sequence.copy()
            for but in self.sequence: #flashing sequence
                Fl.add_timeout(1.0*self.times, self.blink, but)
                self.times += 1
            Fl.add_timeout(5.0 + 1.0*self.times, self.timer) #time out timer
        
    def blink(self, but):#press the button for flashing
        self.sound(but)
        self.buttons[but].value(1)
        Fl.add_timeout(0.5, self.blunk, but)
    
    def blunk(self, but):#depress the button for flashing
        self.buttons[but].value(0)

    def timer(self):#5 sec answer timer
        fl_message('You ran out of time')
        self.best.value(str(self.score))
        
    def game(self, w, num):
        if num == self.sequence2[0]: #correct choice
            self.sound(num)
            self.sequence2.pop(0)
            Fl.remove_timeout(self.timer)
            if len(self.sequence2) == 0: #if the whole sequence is pressed
                self.score += 1
                self.current.value(str(self.score))#update score
                self.seq()
        else: #wrong choice
            self.best.value(str(self.score))
            skull = MediaPlayer('error.mp3')
            skull.play()
    
if __name__ == '__main__':
    Fl.scheme('plastic')
    game = simon(600, 600, "Simon")
    game.show()
    Fl.run()

