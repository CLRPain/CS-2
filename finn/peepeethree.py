from fltk import *
import os
import subprocess as sub
import signal as sig

def opens(wid):
	global songdict
	d = fl_dir_chooser("Import Songs",".")
	files = os.listdir(d)
	for song in files:
		names = []
		pathlist = []
		if song[-4:] in (".mp3", ".ogg", ".wav"):
			pathlist.append(os.path.join(d,song))
			names.append(song[:-4])
			brow.add(song)
			songdict[names[0]] =  pathlist[0]
			
def clear(wid):
	songdict.clear()
	brow.clear()

def brow_cb(wid, x):
    global mp3
    pos=brow.value()+x 
    print(pos)
    mp3=brow.text(pos) # starts at 1
    if x != 0:
        sub.Popen.kill(pid)
        sub.Popen(['vlc', '--intf', 'dummy', mp3])
    out.value(mp3)
    
def play_cb(wid):
    global mp3,play,pid
    if play == 0:
	    pid = sub.Popen(['vlc', '--intf', 'dummy', mp3])

def stop_cb(wid):
    return #stop button

def rem_cb(wid):
    removed = brow.value()
    goner = str(brow.text(removed))
    dictgoner = (goner[:-4])
    brow.remove(removed)
    songdict.pop(dictgoner)

def loop_cb(wid):
    return #loop song


mp3 = ""
play = 0
songdict = {}
win = Fl_Window(400,400,420,540,"Vibration")

win.begin()
ph = win.h() -70
backbut = Fl_Button(0, ph, 70, 70, "@|<")
playbut = Fl_Button(70, ph, 70, 70, "@>")
forbut = Fl_Button(140, ph, 70, 70, "@>|")
stopbut = Fl_Button(210, ph, 70, 70, "@square")
rembut = Fl_Button(280, ph, 70, 70, "@undo")
loopbut = Fl_Button(350, ph, 70, 70, "@refresh")
out = Fl_Output(0, 30, win.w(), 30)
brow = Fl_Hold_Browser(0, 60, win.w(), win.h()-130)
playbut.tooltip("Play Selected Song")
backbut.tooltip("Play Previous Song")
forbut.tooltip("Play Next Song")
stopbut.tooltip("Pause Current Song")
rembut.tooltip("Remove Selected Song")
mb = Fl_Menu_Bar(0,0,win.w(),30)
mb.add("File/Open",0,opens)
mb.add("File/Clear",0,clear)
win.end()

brow.callback(brow_cb, 0)
backbut.callback(brow_cb, -1)
playbut.callback(play_cb)
forbut.callback(brow_cb, 1)
stopbut.callback(stop_cb)
rembut.callback(rem_cb)
loopbut.callback(loop_cb)

win.resizable(win)

win.show()
Fl.run()
