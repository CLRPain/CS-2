from fltk import *

def dothis():
	but.do_callback()
	
def but_cb(w):
	if but.image()!=None:
		print('remove image')
		but.image(None)
		but.redraw()
	else:
		print("put image")
		but.image(pic)
		but.redraw()
	Fl.repeat_timeout(0.8, dothis)
	
def but2_cb(w):
		Fl.remove_timeout(dothis)
win = Fl_Window(500,100,300,400,'My GUI')
win.begin()
but = Fl_Button(100,90,100,110)
but.align(FL_ALIGN_TOP)
but2 = Fl_Button(100,250,70,30,'Stop')
win.end()

but.callback(but_cb)
but2.callback(but2_cb)
pic=(Fl_PNG_Image("cat.png")).copy(but.w(),but.h())


win.show()
Fl.run()
