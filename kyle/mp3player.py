# pyright: reportOptionalMemberAccess=false, reportWildcardImportFromLibrary=false
import os
import vlc
from fltk import *

def opens(wid):
    global songdict, pathlist, d
    mediaList = vlc.libvlc_media_list_new()
    d = fl_dir_chooser("Import Songs",".")
    files = os.listdir(d)
    for song in files:
        if song[-4:] in (".mp3", ".ogg", ".wav"):
            pathlist.append(os.path.join(d,song))
            names.append(song[:-4])
            brow.add(song)
            songdict[names[0]] =  pathlist[0]
            mediaList.add_Media(mediaPlayer.media_new())

def brow_cb(wid):
    global pos, mp3
    pos=brow.value() 
    file = brow.text(pos)
    mp3 = vlc.Media(pathlist[pos-1])
    out.value(file)
        
def move_cb(wid ,x):
    global mp3, pathlist, pos
    pos += x
    if pos%(len(pathlist)+1) == 0:
        pos = 1
        print('loop')
    player.stop()
    file = brow.text(pos)
    brow.select(pos)
    print(pos)
    mp3 = vlc.Media(pathlist[pos-1])
    out.value(file)
    player.set_media(mp3)
    player.play()

def clear(wid):
    songdict.clear()
    brow.clear()

def play_cb(wid):
    if player.is_playing() == 0:
        player.vlc.add_media(mp3)
        player.play() 
        player.set_time(240000)
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
    global looping
    

play = 0
songdict={}
names = []
pathlist = []
looping = False
mediaPlayer = vlc.Instance()
player = vlc.libvlc_media_list_player_new(mediaPlayer)
win = Fl_Window(0, 0, 700, 540, 'MP3 Player')

ph=win.h()-70

win.begin()
backbut = Fl_Button(0, ph, 70, 70, "@|<")
playbut = Fl_Button(70, ph, 70, 70, "@>")
forbut = Fl_Button(140, ph, 70, 70, "@>|")
stopbut = Fl_Button(210, ph, 70, 70, "@||")
rembut = Fl_Button(280, ph, 70, 70, "@undo")
loopbut = Fl_Button(350, ph, 70, 70, "@refresh")
vol = Fl_Hor_Nice_Slider(430, ph, 200, 30)
prop = Fl_Hor_Value_Slider(430, ph + 40, 200, 30)
out = Fl_Output(0, 30, win.w(), 30)
brow = Fl_Hold_Browser(0, 60, win.w(), win.h()-130)
playbut.tooltip("Click on an Audio file and press play")
forbut.tooltip("Play previous song")
backbut.tooltip("Play next song")

mb = Fl_Menu_Bar(0,0,win.w(),30)
mb.add("File/Open",0,opens)
mb.add("File/Clear",0,clear)
win.end()

backbut.callback(move_cb, -1)
playbut.callback(play_cb)
forbut.callback(move_cb, 1)
stopbut.callback(stop_cb)
rembut.callback(rem_cb)
loopbut.callback(loop_cb)
brow.callback(brow_cb)



win.show()
Fl.run()
