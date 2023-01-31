from fltk import*

w = Fl_Window(500,100,300,400, "Pack Demo")
w.begin()

p1 = Fl_Pack(0,0,300,400)
p1.begin()
but1 = Fl_Button(0,0,0,50)
but2 = Fl_Button(0,0,0,50)
but3 = Fl_Button(0,0,0,50)
p1.end()
#p1.type(FL_HORIZONTAL)
p1.type(FL_VERTICAL)
p1.spacing(5)

w.end()

Fl.scheme("gtk+")
w.show()
Fl.run()
