from fltk import *

def but_cb(wid):
	cel=int(inp.value())
	far=(cel*9/5)+32
	out.value(str(far))
	
win = Fl_Window(300,400,400,400, 'Temperature Calculator')
win.begin()

p=Fl_Pack(0,0,win.w(),win.h())
p.begin()

inp=Fl_Input(0,0,0,80)
inp.textsize(24)
out=Fl_Output(0,0,0,80)
out.textsize(24)
but = Fl_Button(0,0,0,80, 'Covert C->F')
but.callback(but_cb)

p.end()
p.type(FL_VERTICAL)
p.spacing(50)

win.end()
win.show()
Fl.run()
