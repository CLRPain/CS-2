from fltk import *
import random
import os
import vlc


def dirchooser_cb(wid): #Directory Chooser
	global songnames,d
	brow.clear() # Clears the browser and puts new song names in
	d=fl_dir_chooser('Pick a file','')
	if d==None:
		return []
	fnames=os.listdir(d)
	songnames=[]
	for name in fnames: # Only accepting common sound files
		if name[-4:] in ('.mp3','.ogg',):
			songnames.append(os.path.join(d,name))
	for x in range(len(songnames)): # Dictionary of song paths and song names
		brow.add(fnames[x])
		SL[fnames[x]]=songnames[x]
	win.redraw()
	
def brow_cb(wid): # If song is clicked
	global song,cursong,firstsong,songnum
	pausebut.label('@+3||')
	song.stop() # Making sure that only one song plays at a time
	songnum=brow.value()
	cursong=brow.text(songnum)
	song=vlc.MediaPlayer(SL[cursong])
	song.play()
	firstsong=False
	out.value(cursong) # Shows selected song at top
	scrollbar()

# BUTTON CALLBACKS
	
def pp_cb(wid): # Pause and play function
	global song
	if song.is_playing() == 1:
		pausebut.label('@+3>')
		song.pause()
	if song.is_playing() == 0:
		pausebut.label('@+3||')
		song.pause()
	win.redraw()
	#Fl remove slider timeout
	
def nextprev_cb(wid,n): # Next and previous button function
	global song,cursong,songnum,songnames
	song.stop()
	pausebut.label('@+3||')
	if songnum == 1 and n == -1: # If previous is clicked on first song
		x = 2 + len(songnames)
		songnum = n % x
	if songnum == len(songnames) and n == 1: # If next is clicked on last song
		songnum = 1
	else:
		songnum = songnum + n
	cursong=brow.text(songnum)
	song=vlc.MediaPlayer(SL[cursong])
	song.play()
	brow.select(songnum) #Highlights current song
	out.value(cursong) # Shows selected song at top
	#Slider
	
def stop_cb(wid): # Stop function
	global song
	song.stop()
	
	
def replay_cb(wid): # Replay song function
	global song,cursong
	pausebut.label('@+3||')
	if song.is_playing() == 1:
		song.set_time(0)
	else:
		song=vlc.MediaPlayer(SL[cursong])
		song.set_time(0)
		song.play()
		
def slid():
	return
# MENU BAR FUNCTIONS

def delsel(wid): # Delete selected song from list
	global songnum, song, cursong
	song.stop()
	brow.remove(songnum)
	out.value(None)
	SL.pop(cursong)
	
def delall(wid): # Delete all songs from browser
	global song
	song.stop()
	brow.clear()
	out.value(None)
	SL.clear()
	song=vlc.MediaPlayer()

def pausehk(wid): # Shows the current pause shortcut
	fl_message(f'Current pause shortcut is "{pause}"')
	
def nexthk(wid): # Shows the current next button shortcut
	fl_message(f'Current next shortcut is "{nexth}"')
	
def prevhk(wid): # Shows the current previous button shortcut
	fl_message(f'Current previous shortcut is "{prev}"')

def replayhk(): # Shows the current replay button shortcut
	fl_message(f'Current replay shortcut is "{replay}"')
	
def stophk(): # Shows the current stop button shortcut
	fl_message(f'Current stop shortcut is "{stop}"')
	
def fileloc_cb(wid): # Opens the directory
	global cursong,d
	if d=='':
		print('No current selected directory')
		return
	else:
		os.system(f'xdg-open "%s"' % d) # I googled how to do this

def closewin(widget): # Refering to Exit on menubar
	global song
	song.stop()
	win.hide()

def scrollbar():
	global song
	slider.value(0)
	print(song.get_length)
	double = int(str(song.get_length))/100

	slider.maximum(double)


		

	
# Change these to change short cut buttons:

pause=']' 
nexth='\\'
prev='['
replay='{'
stop='|'


#Varibles
firstsong=True
SL={} # Song list
cursong='' #Current song
song=vlc.MediaPlayer()
songnum=0 # Song number in the list (Top to bottom)
songnames=[]
d='' # Directory
wc=fl_rgb_color(125,203,184) # Window color


win=Fl_Window(100,100,400,550,'MP3 Player')
win.color(wc)
win.begin()

c=fl_rgb_color(91, 233, 199) # Button color

brow=Fl_Hold_Browser(50,80,300,260,'Songs')

out=Fl_Output(50,40,300,30) # Box at top to display current song

menu=Fl_Menu_Bar(0,0, win.w(),25)


# Menubar:
menu.add("File/Open folder",0,dirchooser_cb)
menu.add("File/Open location",0,fileloc_cb)
menu.add("File/Exit",FL_F+5,closewin)

menu.add("Edit/Remove",0,delsel)
menu.add("Edit/Remove All",0,delall)

menu.add("Shortcuts/Pause",0,pausehk)
menu.add("Shortcuts/Next",0,nexthk)
menu.add("Shortcuts/Previous",0,prevhk)
menu.add("Shortcuts/Replay",0,prevhk)
menu.add("Shortcuts/Stop",0,prevhk)

# Buttons:
pausebut=Fl_Button(177,405,51,51,'@+3||')
pausebut.box(FL_OSHADOW_BOX)
pausebut.color(c)

nextbut=Fl_Button(237,415,40,40,'@+1>|')
nextbut.box(FL_OSHADOW_BOX)
nextbut.color(c)

prevbut=Fl_Button(127,415,40,40,'@+1|<')
prevbut.box(FL_OSHADOW_BOX)
prevbut.color(c)

replaybut=Fl_Button(50,370,75,30,'@reload')
replaybut.box(FL_SHADOW_BOX)
replaybut.color(c)

stopbut=Fl_Button(277,370,75,30,'@square')
stopbut.box(FL_SHADOW_BOX)
stopbut.color(c)

slider=Fl_Hor_Value_Slider(50, 475, 300, 25)

win.end()




# Tooltips

pausebut.tooltip("Play/Pause")

nextbut.tooltip("Next")

prevbut.tooltip("Previous")

replaybut.tooltip("Replay")

stopbut.tooltip("Stop")




# Callbacks
stopbut.callback(stop_cb)

nextbut.callback(nextprev_cb,+1) # +1 song up

prevbut.callback(nextprev_cb,-1) # -1 song down

pausebut.callback(pp_cb)

replaybut.callback(replay_cb)

brow.callback(brow_cb)


# Shortcuts
pausebut.shortcut(ord(pause))

nextbut.shortcut(ord(nexth))

prevbut.shortcut(ord(prev))

replaybut.shortcut(ord(replay))

stopbut.shortcut(ord(stop))


win.resizable(win)
Fl.scheme("gleam")
win.show()
Fl.run()
