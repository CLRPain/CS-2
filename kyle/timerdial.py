from fltk import *

def ticktock():
    time=int(display.value())
    time=time+1
    display.value(str(time))
    dial.value(dial.value()+6.0) # 6 degrees/sec
    Fl.repeat_timeout(1.0,ticktock)

def start_cb(widget):
    Fl.add_timeout(1.0, ticktock)
    butstart.deactivate()
    butstop.activate()

def stop_cb(widget):
    Fl.remove_timeout(ticktock)
    butstart.activate()
    butstop.deactivate()

def reset_cb(widget):
    dial.value(0.0)
    display.value('0')

w=Fl_Window(400,50, 300,300)
w.begin()
butstart=Fl_Button(20,20,70,30,"Start")
butstop=Fl_Button(20,100,70,30,"Stop")
butreset=Fl_Button(20,180,70,30,"Reset")
display=Fl_Output(100,100,70,30)
dial=Fl_Dial(150,170,90,90)
dial.type(FL_FILL_DIAL)
#dial.type(FL_LINE_DIAL)
dial.color(FL_WHITE,FL_RED)
dial.angle1(180)
dial.angle2(181)
w.end()

butstop.deactivate()
display.value('0')
butstart.callback(start_cb)
butstop.callback(stop_cb)
butreset.callback(reset_cb)
Fl.scheme('gleam') #plastic, gtk+, gleam, normal (default)
w.show()
Fl.run()
