from fltk import *

def dothis(ft):
    print("aaaaa")
    Fl.repeat_timeout(ft, dothis, ft-0.5)
    
def but_cb(w):
    but.image(pic.copy(but.w(), but.h()))
    but.redraw()
    Fl.remove_timeout(dothis)

win = Fl_Window(500, 100, 300, 400, "my gui")
win.begin()
but = Fl_Button(100, 90, 100, 110)
win.end()

but.callback(but_cb)
pic = Fl_PNG_Image("electro.png")

Fl.add_timeout(1.0, dothis, 2.0)


win.show()
Fl.run()


'''
from fltk import *

def dothis(v):
    print(v)

    
def but_cb(w):
    Fl.remove_timeout(dothis, 2)

win = Fl_Window(500, 100, 300, 400, "my gui")
win.begin()
but = Fl_Button(100, 90, 100, 110)
win.end()

but.callback(but_cb)

Fl.add_timeout(2.0, dothis, 1)
Fl.add_timeout(4.0, dothis, 2)
Fl.add_timeout(6.0, dothis, 3)


win.show()
Fl.run()

'''