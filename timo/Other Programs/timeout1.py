from fltk import *

def dothis(a):
	print('DONT PRESS THE BUTTON')
	Fl.repeat_timeout(1.0,dothis,1)
	
def but_cb(w):
	print('wow you actually pressed it...')
	but.image(pic.copy(but.w(),but.h()))
	Fl.remove_timeout(dothis)

win = Fl_Window(500,100,300,400,'My GUI')
win.begin()
but=Fl_Button(100,90,100,110)
win.end()

but.callback(but_cb)
pic=Fl_PNG_Image("cat.png")

Fl.add_timeout(3.0, dothis,1)

win.show()
Fl.run()

