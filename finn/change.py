from fltk import *

pic = Fl_PNG_Image("bruhgrams.png")
pic = pic.copy(100,40)
def but_cb(wid):
	print("done")
	wid.color(FL_GREEN)
	wid.image(pic)
	wid.redraw()




win = Fl_Window(300,400,400,400)
win.begin()
but1 = Fl_Button(0,0,100,40, "1")
but2 = Fl_Button(0 , 50,100,40, "2")
win.end()

but1.callback(but_cb)
but2.callback(but_cb)

win.show()
Fl.run()
