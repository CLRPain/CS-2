from fltk import *
from random import randrange
import vlc

class simon(Fl_Window):
    sequence = []
    score = 0
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        self.begin()
        self.buttons = []
        
        red = Fl_Button(0, 0, 150, 150)#up left
        blue = Fl_Button(self.w()-150, 0, 150, 150)#up right
        green = Fl_Button(0, self.h()-150, 150, 150)#down left
        yellow = Fl_Button(self.w()-150, self.h()-150, 150 ,150)#down right
        startbut = Fl_Button(self.w()//2-40, self.h()//2-40 ,80 ,80, "Start")
        
        red.color(FL_DARK_RED)
        blue.color(FL_DARK_BLUE)
        green.color(FL_DARK_GREEN)
        yellow.color(FL_DARK_YELLOW)
        
        red.down_color(FL_RED)
        blue.down_color(FL_BLUE)
        green.down_color(FL_GREEN)
        yellow.down_color(FL_YELLOW)
        
        
        self.end()
        
        self.buttons.append(red)
        self.buttons.append(blue)
        self.buttons.append(green)
        self.buttons.append(yellow)
        self.buttons[0].callback(self.sound, 0)
        self.buttons[1].callback(self.sound, 1)
        self.buttons[2].callback(self.sound, 2)
        self.buttons[3].callback(self.sound, 3)

        startbut.callback(self.start)
    
    def sound(self, w, v):
        sounds = ['red.mp3', 'blue.mp3', 'green.mp3', 'yellow.mp3']
        #sounds = ['Quick Sound.mp3', 'Quick Sound.mp3', 'Quick Sound.mp3', 'Quick Sound.mp3']
        effects = vlc.MediaPlayer(sounds[v])
        effects.play()
            
    def start(self, w):
        Fl.add_timeout(0.5, self.seq)
        
    def seq(self):
        print(simon.score)
        seqint = randrange(0, 4)
        simon.sequence.append(seqint)
        Fl.repeat_timeout(0.5, self.seq)
        if len(simon.sequence) >= simon.score:
            Fl.remove_timeout(self.seq)
            print(simon.sequence)

        
game = simon(400, 400, "Frank")
game.show()
Fl.run()