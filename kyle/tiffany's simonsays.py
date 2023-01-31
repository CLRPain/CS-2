from fltk import *
import vlc

import random
import time

class game(Fl_Window):
    def __init__(self, w, h, label):
        ww=500
        wh=500
        self.win= Fl_Window(300, 400, ww, wh, 'Simon Says')
        self.display=Fl_Output(215,15,70,30)
       
        
        bw =int(ww/3)
        bh=int(wh/3)

        #self.win.begin()
        self.flash_seq=[]
        self.butclicked=[]
        self.TIMESTARTED=False
        self.timesflashed=0
        self.but_pressed=[]

        self.r=Fl_Button(int(ww/2-bw-30), int(wh/2-bh-30), bw,bh,'') 
        self.r.color(FL_RED)
        self.r.callback(self.button_cb, 0)
        self.r.sound=vlc.MediaPlayer("red.mp3")


        self.y=Fl_Button(int(ww/2+30), int(wh/2-bh-30), bw,bh,'') 
        self.y.color(FL_YELLOW)
        self.y.callback(self.button_cb, 1)
        self.y.sound=vlc.MediaPlayer("yellow.mp3")


        self.g=Fl_Button(int(ww/2-bw-30), int(wh/2+30), bw,bh,'') 
        self.g.color(FL_GREEN)
        self.g.callback(self.button_cb, 2)
        self.g.sound=vlc.MediaPlayer("green.mp3")


        self.b=Fl_Button(int(ww/2+30), int(wh/2+30), bw,bh,'') 
        self.b.color(FL_BLUE)
        self.b.callback(self.button_cb, 3)
        self.b.sound=vlc.MediaPlayer("blue.mp3")
    
        
        self.but_list=[self.r,self.y,self.g,self.b]
        for x in range(4):
            self.but_list[x].deactivate()

        self.butstart= Fl_Button(200,220,100,61,'START')

        # self.display.value('0')
        self.butstart.callback(self.start_cb)

        self.win.end()
        self.win.show()

    def ticktock(self):
        time=int(self.display.value())
        time=time+1
        self.display.value(str(time))
        Fl.repeat_timeout(1.0, self.ticktock)

    def start_cb(self, widget):
        if self.TIMESTARTED==False:
            self.display.value('0')
            Fl.add_timeout(1.0, self.ticktock)
            self.TIMESTARTED=True
        #self.butstart.deactivate()
        self.flash_seq.append(random.randrange(4))
        for x in range(4):
            self.but_list[x].deactivate()
        Fl.add_timeout(0.5,self.flash,0)
        # Fl.add_timeout(time, self.enable_buttons)

    def flash(self, num):
        if num<len(self.flash_seq):
            button=self.but_list[self.flash_seq[num]]
            color=self.but_list[self.flash_seq[num]].color()
            self.but_list[self.flash_seq[num]].color(FL_WHITE)
            self.win.redraw()
            print(self.flash_seq[num], num)
            print(self.r.color(), self.y.color(), self.g.color(), self.b.color())
            self.win.redraw()
            Fl.repeat_timeout(0.5, self.flash, num+1)
            Fl.add_timeout(0.4, self.unflash, [button, color])

    def unflash(self, var):
        button=var[0]
        color=var[1]
        button.color(color)
        self.win.redraw()
        self.timesflashed=self.timesflashed+1
        print(self.timesflashed)
        if self.timesflashed==len(self.flash_seq):
            print('done')
            self.enable_buttons()
            self.timesflashed=0

    def enable_buttons(self):
        for x in range(4):
            self.but_list[x].activate()

    def button_cb(self, widget, num):
        widget.sound.stop()
        widget.sound.play()
        if len(self.but_pressed) <= len(self.flash_seq):
            self.but_pressed.append(num)
            print(self.but_pressed)
            if self.but_pressed == self.flash_seq[0:len(self.but_pressed)]:
                print('good')
            else:
                print('you lose')
                self.but_pressed=[]
                self.flash_seq=[]
                #self.butstart.activate()
                for x in range(4):
                    self.but_list[x].deactivate()
                Fl.remove_timeout(self.ticktock)
                self.TIMESTARTED=False
                return

            if self.but_pressed==self.flash_seq:
                print('passed')
                self.but_pressed=[]
                self.flash_seq.append(random.randrange(4))
                for x in range(4):
                    self.but_list[x].deactivate()
                Fl.add_timeout(0.5,self.flash,0)
                return

if __name__=='__main__':
    win=game(500,500, 'Simon Says')
    Fl.run()