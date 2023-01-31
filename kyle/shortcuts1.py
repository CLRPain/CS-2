from fltk import *
def but_cb(wid):
    print('event')

win = Fl_Window(0, 0, 400, 400, 'shortcuts')
win.begin()
but = Fl_Button(10, 10, 170, 50, 'ok')
win.end()
but.shortcut(FL_CTRL | ord('a')) #works
but.shortcut(FL_META | ord('a')) #works with windows key 
but.shortcut(FL_Left)
but.shortcut(FL_ALT|FL_F+6)
but.shortcut(ord('6'))
but.shortcut(FL_KP+6)
#check on website