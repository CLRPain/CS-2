from fltk import *
import os
import vlc



def opens(wid):
	global songdict
	d = fl_dir_chooser("Import Songs",".")
	files = os.listdir(d)
	for song in files:
		names = []
		pathlist = []
		if song[-4:] in (".mp3", ".ogg", ".wav"):
			pathlist.append(os.path.join(d,song))
			pathlist2.append(song[:-4])
			names.append(song[:-4])
			browlist.append(song[:-4])
			songdict[names[0]] =  pathlist[0]
	browlist.sort()
	pathlist2.sort()
	for song in browlist:
		brow.add(song)
def clear(wid):
	pathlist2.clear()
	songdict.clear()
	brow.clear()

def brow_cb(wid, x):
	global mp3
	pos=brow.value() + x
	num = len(pathlist2)
	if pos == num+x and x == 1:
		pos = 1
		brow.select(pos)
		filez = brow.text(pos)
		query = songdict.get(filez)	
		mp3 = vlc.Media(query)
		out.value(filez)
		play_cb(wid)
	elif pos == 0 and x == -1:
		pos = num
		brow.select(pos)
		filez = brow.text(pos)
		query = songdict.get(filez)	
		mp3 = vlc.Media(query)
		out.value(filez)
		play_cb(wid)
	else:
		pos=brow.value() + x
		brow.select(pos)
		filez = brow.text(pos)
		query = songdict.get(filez)	
		mp3 = vlc.Media(query)
		out.value(filez)
		play_cb(wid)
	

def play_cb(wid):
	print(wid)
	if player.is_playing() == 0:
		player.set_media(mp3)
		player.play() 
	else:
		player.stop()
		player.set_media(mp3)
		player.play() 


def stop_cb(wid):
	player.stop()

def rem_cb(wid):
    removed = brow.value()
    goner = str(brow.text(removed))
    dictgoner = (goner[:-4]) 
    brow.remove(removed)
    songdict.pop(dictgoner)

def loop_cb(wid):
    return #loop song

pathlist2 = []
browlist = []
player = vlc.MediaPlayer()
oldmp3 = ""
mp3 = ""
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
mb.add("File/Open",ord('o'),opens)
mb.add("File/Clear",ord('c'),clear)
win.end()

brow.callback(brow_cb, 0)
backbut.callback(brow_cb, -1)
playbut.callback(play_cb)
forbut.callback(brow_cb, 1)
stopbut.callback(stop_cb)
rembut.callback(rem_cb)
loopbut.callback(loop_cb)
playbut.shortcut(ord("p"))
forbut.shortcut(ord("n"))
backbut.shortcut(ord("b"))
stopbut.shortcut(ord("s"))
rembut.shortcut(ord("r"))
win.resizable(win)

win.show()
Fl.run()
