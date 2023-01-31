from fltk import *

def but_cb(wid):
    cel=int(inp.value())
    #cel=int(fl_input('Enter celcius: ')) # Alternative is pop-up input dialog 
    far=(cel*9/5)+32
    out.value(str(far))

win = Fl_Window(300,400, 400,300, 'Input Demo')
win.begin()

p=Fl_Pack(0,0,win.w(),win.h())
p.begin()

inp=Fl_Input(0,0,0,50,'Celcius')
inp.align(FL_ALIGN_BOTTOM_LEFT)
inp.textsize(24)
inp.textcolor(218)
inp.labelsize(20) #Celcius
inp.labelcolor(220)
inp.color(247)

out=Fl_Output(0,0,0,50,'Farenheit')
out.align(FL_ALIGN_BOTTOM_LEFT)
out.textsize(24)
out.labelsize(20) #Farenheit
out.labelcolor(100)
out.color(127)

but = Fl_Return_Button(0,0,0,80,'Conve&rt C->F') #the amperasand be a shortcut matey because alt and and button is cool
but.callback(but_cb)

p.end()
#p.type(FL_VERTICAL) #this is wrong in video
p.type(Fl_Pack.VERTICAL) #corrected
p.spacing(30)

win.end()
win.show()
Fl.run()

