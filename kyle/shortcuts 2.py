from fltk import *

def foo(event):
    if event == FL_SHORTCUT:
        pressed = Fl.event_key()
        print(f'you pressed the letter {chr(pressed)}')

#see Enumerations for other Fl::event_key() Values

win=Fl_Window(200,200)
Fl.add_handler(foo)
win.show()
Fl.run()