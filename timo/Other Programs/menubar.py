from fltk import *


def closewin(widget):
        print("shutting down")
        w.hide()

def filecb(widget):
        fl_message("this is the filecb")

def editcb(widget):
        fl_message("this is the editcb")

def helpcb(widget):
        fl_message("I am in your walls :)")

def opencb(widget):
        fl_message("this is the opencb")

w = Fl_Window(600, 50, 300, 300, "XD")
w.begin()
menu=Fl_Menu_Bar(0,0, w.w(),25)
menu.add("File/Open",0,opencb)
menu.add("File/Exit",FL_F+5,closewin)
menu.add("Edit/Undo ",FL_F+2,editcb)
menu.add("Edit/Redo ",FL_F+2,editcb)
menu.add("Edit/Preferences ",FL_F+2,editcb)
menu.add("File/Hi :)",FL_F+6,helpcb)

menu.add("Hel&p/A&bout",ord('x'),helpcb)
menu.add("Hel&p/Software/History",0,helpcb)
menu.add("Hel&p/Software/License",0,helpcb)

but=Fl_Button(50, 50, 200, 200,'Hi!')
but.color(FL_RED)
w.end()
w.callback(closewin)
Fl.scheme("gtk+")
w.show()
Fl.run()
