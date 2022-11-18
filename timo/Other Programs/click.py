from fltk import *

def but_cb(wid): #Wid is the widget which receives the event
	print('Click!')
	
	wid.image(pic)
	#wid.color(FL_GREEN)
	#wid.redraw
	
	
pic = Fl_PNG_Image('cat.png')
pic=pic.copy(200,400)

win = Fl_Window(300,400,400,800)
win.begin()
but1 = Fl_Button(0,0,200,400,'Click Me!')
but2 = Fl_Button(0,450,200,400,'Button2')
win.end()

but1.callback(but_cb)
but2.callback(but_cb)
win.show()
Fl.run()

# # # A call back is a funtion which is executed when a widget recieves an event.
