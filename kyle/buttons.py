from fltk import*
pic = Fl_PNG_Image("sus.png")
pic = pic.copy(100, 70)

def but_cd(wid):
	print("button pressed")
	wid.image(pic)
	wid.redraw()
	

ww = 700
wh = 500
win = Fl_Window(100, 100, ww, wh)
win.begin()
bw = int(ww/2)
bh = int(wh/2)
but1 = Fl_Button(0, 0, bw, bh, "1")
but2 = Fl_Button(bw, 0, bw, bh, "2")
but3 = Fl_Button(0, bh, bw, bh, "3")
but4 = Fl_Button(bw, bh, bw, bh, "4")
print(Fl.w(), Fl.h())
but1.callback(but_cd)
but2.callback(but_cd)
but3.callback(but_cd)
but4.callback(but_cd)
win.show()
Fl.run()
