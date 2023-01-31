from fltk import *

def foo(event):
    if event == FL_SHORTCUT:
        pressed = Fl.event_key()
        if pressed == ord('a'):
            print('you pressed the letter a')
            return 1
        elif pressed == FL_Enter:
            print('you pressed Enter')
            return 1
        else:
            return 0
    else:
        return 0

#see Enumerations for other Fl::event_key() Values

win=Fl_Window(200,200)
Fl.add_handler(foo)
win.show()
Fl.run()
