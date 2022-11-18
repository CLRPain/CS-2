from fltk import *

def brow_cb(wid):
    pos=brow.value()
    name=brow.text(pos) # starts at 1
    out.value(name)


def but_cb(wid):
    fname= fl_file_chooser('Open File','*.txt',None)
    f=open(fname,'r')
    for name in f:
        brow.add(name[:-1])#[:-1] omit newline char from file
    f.close()

def inp_cb(wid):
    name=wid.value()
    brow.add(name)
    wid.value('')
    wid.take_focus()

def save_cb(wid):
	f=open('names.txt', 'w')
	for x in range(1,brow.size()+1):
		f.write(brow.text(x)+'\n')
	f.close()


win=Fl_Window(100,100,400,500,'FL_Browser Example')
win.begin()
brow=Fl_Hold_Browser(50,50,300,300,'Names')
out=Fl_Output(50,10,300,30)
but=Fl_Button(50,360,70,25,'Open')
savbut=Fl_Button(280,360,70,25,'Save')
inp=Fl_Input(50,400,300,30,'Name:')
win.end()

brow.callback(brow_cb)
but.callback(but_cb)
inp.callback(inp_cb)
savbut.callback(save_cb)

inp.take_focus()

win.show()
Fl.run()

