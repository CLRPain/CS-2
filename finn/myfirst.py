from fltk import * #this allows for you to call functions without referencing the module name first)
ww = 300
wh = 300
bw = 130
bh = 120
x = int(ww / 2 - bw / 2)
y = int(wh / 2 - bh / 2)
win = Fl_Window(450,450, ww, wh, "Winning")
but = Fl_Button(x,y,bw,bh, "Play")
#but.color(FL_CYAN) this works but i prefer the other way below
but.color(fl_rgb_color(123,17,223), FL_RED)
but.labelcolor(fl_rgb_color(255,127,45))
but.labelsize(25)
#but.box(FL_RSHADOW_BOX) does not do anything while scheme is active
win.end()
win2 = Fl_Window(150,450,300, 300, "Bonus")
win2.end()


but.align(FL_ALIGN_BOTTOM | FL_ALIGN_INSIDE)

Fl.scheme("gtk+")
win.show() #screen coords and size dimensions
win2.show()
Fl.run()
#import fltk works too but slower
#const char * is a string


