from fltk import *
from vlc import MediaPlayer
import random

class game(Fl_Window):
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        self.display = Fl_Output(215,15,70,30)
        self.display.value('0')
        
        bw = w//3
        bh = h//3

        self.begin()
        self.flash_seq=[]
        self.but_list = []
        self.soundlist = ['red.mp3', 'yellow.mp3', 'green.mp3', 'blue.mp3']
        self.score = 0
        self.audio = MediaPlayer()

        r=Fl_Button(int(w/2-bw-30), int(h/2-bh-30), bw,bh) 
        y=Fl_Button(int(w/2+30), int(h/2-bh-30), bw,bh) 
        g=Fl_Button(int(w/2-bw-30), int(h/2+30), bw,bh) 
        b=Fl_Button(int(w/2+30) ,int(h/2+30) ,bw ,bh) 
        
        r.color(FL_DARK_RED)
        r.down_color(FL_RED)
        y.color(FL_DARK_YELLOW)
        y.down_color(FL_YELLOW)
        g.color(FL_DARK_GREEN)
        g.down_color(FL_GREEN)
        b.color(FL_DARK_BLUE)
        b.down_color(FL_BLUE)
        
        self.but_list.append(r)
        self.but_list.append(y)
        self.but_list.append(g)
        self.but_list.append(b)
        
        self.but_list[0].callback(self.button_cb, 0)
        self.but_list[1].callback(self.button_cb, 1)
        self.but_list[2].callback(self.button_cb, 2)
        self.but_list[3].callback(self.button_cb, 3)

        self.butstart = Fl_Button(200,220,100,61,'START')

        self.butstart.callback(self.start_cb)

        self.resizable(self)
        self.end()

    def start_cb(self, widget):
        if len(self.flash_seq) > 0:
            self.flash_seq.clear()
        self.flash_seq.append(random.randrange(4))
        self.flash_seq2 = self.flash_seq.copy()
        Fl.add_timeout(0.5, self.flash, self.flash_seq[0])
        Fl.add_timeout(5.0 + 1.0, self.timer)

    def sound(self, num):
        self.audio.stop()
        self.audio = MediaPlayer(self.soundlist[num])
        self.audio.play()
        
    def timer(self):
        self.audio = MediaPlayer('error.mp3')
        self.audio.play()
        self.display.value(str(self.score))
        fl_message("you suck badly")
        
    def flash(self, num):
        self.sound(num)
        self.but_list[num].value(1)
        Fl.add_timeout(0.5, self.unflash, num)

    def unflash(self, num):
        self.but_list[num].value(0)

    def button_cb(self, widget, num):
        print(self.flash_seq2)
        Fl.remove_timeout(self.timer)
        if num == self.flash_seq2[0]:
            Fl.add_timeout(5.0, self.timer)
            self.sound(num)
            self.flash_seq2.pop(0)
            if len(self.flash_seq2) == 0:
                self.score += 1
                self.display.value(str(self.score))
                print('passed')
                self.flash_seq.append(random.randrange(4))
                self.flash_seq2 = self.flash_seq.copy()
                self.times = 1
                for x in self.flash_seq:
                    Fl.add_timeout(1.0*self.times, self.flash, x)
                    self.times += 1
                Fl.add_timeout(5.0 + 1.0*self.times, self.timer)
        else:
            print('you lose')
            self.audio = MediaPlayer('error.mp3')
            self.audio.play()
            self.display.value(str(self.score))

if __name__=='__main__':
    win=game(500, 500, 'Simon Says')
    win.show()
    Fl.run()