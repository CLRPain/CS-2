from fltk import *

class imgflash(Fl_Window):
    def __init__(self, w, h, l):
        Fl_Window.__init__(self, w,h,l)
        self.but = Fl_Button(100,90, 100, 110)
        self.stopbut= Fl_Button(100,250,70,30,"Stop")
        self.end()
        self.but.callback(self.but_cb)
        self.stopbut.callback(self.stopbut_cb)
        self.pic=(Fl_PNG_Image('electro.png')).copy(self.but.w(),self.but.h())
        Fl.add_timeout(1.0, self.tofunc)

    def tofunc(self):
        self.but.do_callback()
        Fl.repeat_timeout(1.0, self.tofunc)

    def stopbut_cb(self, wid):
        Fl.remove_timeout(self.tofunc)

    def but_cb(self,wid):
            if self.but.image()!=None:
                    print("remove image")
                    self.but.image(None)
                    self.but.redraw()
            else:
                    print("put image")
                    self.but.image(self.pic)
                    self.but.redraw()

app= imgflash(400, 300, 'Timeout example 1')
app.show()
Fl.run()
