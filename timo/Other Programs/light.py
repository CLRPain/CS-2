from fltk import *

class seqflash(Fl_Window):

    def __init__(self, w, h, l=None):
        super().__init__(w,h,l)
        self.B=[]
        for x in range(3):
            b=Fl_Box(x*100,0,100,100)
            b.box(FL_UP_BOX)
            b.color(FL_GREEN)
            self.B.append(b)
        self.flashb=Fl_Button(0,100,300,100,'Start Flash')
        self.flashb.callback(self.flashall)
        self.end()


    def boxflash(self,x):
        if self.B[x].color()==FL_GREEN:
            self.B[x].color(FL_RED)
            self.B[x].redraw()
        else:
            self.B[x].color(FL_GREEN)
            self.B[x].redraw()
            return
        Fl.repeat_timeout(1.0,self.boxflash, x)


    def flashall(self,wid):
        for x in range(len(self.B)):
            Fl.add_timeout(2*x, self.boxflash, x)

app=seqflash(300,200,'Flasher')
app.show()
Fl.run()
