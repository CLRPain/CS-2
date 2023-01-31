from fltk import*
#widgets are the only things that must be created between begin and end.
ww = 300
wh = 300
bw = int(ww/2)
bh = int(wh/2)


win = Fl_Window(450,450, ww, wh, "Winning")
but1 = Fl_Button(0,0,bw,bh,"1")
but2 = Fl_Button(bw,0,bw,bh,"2")
but3 = Fl_Button(0,bh,bw,bh,"3")
but4 = Fl_Button(bw,bh,bw,bh,"4")
win.end()


but1.color(FL_RED, FL_RED)
but2.color(FL_BLUE, FL_BLUE)
but3.color(FL_YELLOW, FL_YELLOW)
but4.color(FL_GREEN, FL_GREEN)


print(win.x(), win.y(), but1.x())#button one is from the perspective of the window rather than the screen
print(Fl.w(), Fl.h())


Fl.scheme("gtk+")
win.show()
Fl.run()
