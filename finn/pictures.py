from fltk import *	

pic = Fl_PNG_Image("bruhgrams.png") #creates image
pw = pic.w()
ph = pic.h()
ar = pw/ph
buth= int(300/ar) #ar is aspect ratio

win = Fl_Window(450,450, 300, 300, "picture")
win.begin()
but = Fl_Button(0,0,300,150)
win.end()

pic = pic.copy(but.w(), buth) #resizes image
but.image(pic) #assigns image to button
win.show()
Fl.run()
