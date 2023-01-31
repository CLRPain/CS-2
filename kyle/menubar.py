from fltk import *


def closewin(widget):
        print("shutting down")
        w.hide()

def filecb(widget):
        fl_message("this is the filecb")

def editcb(widget):
        fl_message("this is the editcb")

def helpcb(widget):
        fl_message("this is the helpcb")

def opencb(widget):
        fl_message("this is the opencb")

w = Fl_Window(600, 50, 300, 300, "my gui")
w.begin()
menu=Fl_Menu_Bar(0,0, w.w(),25)
menu.add("File/Open",0,opencb)
menu.add("File/Exit",FL_F+5,closewin)
menu.add("Edit/Undo ",FL_F+2,editcb)
menu.add("Edit/Redo ",FL_F+2,editcb)
menu.add("Edit/Preferences ",FL_F+2,editcb)

menu.add("Hel&p/A&bout",ord('h'),helpcb)
menu.add("Hel&p/S&oftware/Hi&story",0,helpcb)
menu.add("Hel&p/S&oftware/Li&cense",0,helpcb)

w.end()
w.callback(closewin)
w.resizable()
Fl.scheme("plastic")
w.show()
Fl.run()
