from fltk import *

pic = Fl_PNG_Image('longcat.png')

ww=500
wh=500
pw=pic.w()
ph=pic.h()
print(pw,ph)
ar = pw/ph #aspect ratio = w/h
but_h = int(300/ar)

win = Fl_Window(400,300, 700, 700, 'Images')
win.begin()


but = Fl_Button(0,0,300,but_h)

win.end()

'''
pw=pic.w()
ph=pic.h()
print(pw,ph)
ar = pw/ph
pic = pic.copy(int(ar*but.h(),but.h())
'''
pic = pic.copy(but.w(),but.h())
but.image(pic)

win.show()
Fl.run()
