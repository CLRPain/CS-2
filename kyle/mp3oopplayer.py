# https://videolan.videolan.me/vlc/group__libvlc.html Documentation for libvlc
import os
import vlc
from fltk import *
class mp3player:
    
    player = vlc.Instance()
    musicPlayer = player.media_list_player_new() #new media player that plays a list
    musicPlayer.set_playback_mode(vlc.PlaybackMode.loop) #loop the playlist
    mediaList=player.media_list_new() #empty playlist
    win = Fl_Window(700, 540, "MP3 Player")
    
    ph=win.h()-70
    win.begin()
    backbut = Fl_Button(0, ph, 70, 70, "@|<") #control buttons
    playbut = Fl_Button(70, ph, 70, 70, "@>")
    forbut = Fl_Button(140, ph, 70, 70, "@>|")
    stopbut = Fl_Button(210, ph, 70, 70, "@square")
    rembut = Fl_Button(280, ph, 70, 70, "@undo")
    loopbut = Fl_Button(350, ph, 70, 70, "@refresh")
    vol = Fl_Hor_Value_Slider(430, ph+20, 200, 30, "Volume")
    out = Fl_Output(0, 30, win.w(), 30) 
    brow = Fl_Hold_Browser(0, 60, win.w(), win.h()-130)
    looping = False 
    vol.scrollvalue(100, 3, 0, 103) 
    vol.slider_size(0.05) 
    
    def addSongs(self): #adding songs from a directory
        d = fl_dir_chooser("Import Songs",".") #pick directory
        files = os.listdir(d) #all files in the directory
        for songs in files:
            if songs[-4:] in (".mp3", ".ogg", ".wav"): #filter out all non audio files
                path = os.path.join(d, songs) #create full path to file
                mp3player.mediaList.add_media(mp3player.player.media_new(path)) # add media to media list
                mp3player.brow.add(songs) #add media to the browser
        mp3player.musicPlayer.set_media_list(mp3player.mediaList) #set the playlist for list player as the media list
             
    def brow_cb(self): #outputing position and file name when clicked on
        self.pos=mp3player.brow.value() 
        file = mp3player.brow.text(self.pos)
        if file != None: #only accept files names
            mp3player.out.value(file)
        
    def move_cb(self ,x): #move selection with buttons
        pos=mp3player.brow.value()+x #position of the file in browser
        num = mp3player.mediaList.count() #how many media files in the media list
        if x == 1: #move forward
            mp3player.musicPlayer.next() 
            if pos == num+x: #if position is one more than the list length
                pos = 0 #set to beginning
                mp3player.brow.select(1)
                mp3player.out.value(mp3player.brow.text(1))
                return
        elif x == -1: #move backwards
            mp3player.musicPlayer.previous()
            if pos == 0: #if position is one before the start
                pos = num #set position as last in the list
        mp3player.out.value(mp3player.brow.text(pos))
        mp3player.brow.select(pos)
        
    def clearSongs(self): #clear browser and medialist
        mp3player.mediaList.release()
        mp3player.brow.clear()
    
    def play_cb(self): #play the selected song
        mp3player.musicPlayer.play_item_at_index(mp3player.brow.value()-1)

    def stop_cb(self): #pause the song
        mp3player.musicPlayer.pause()

    def rem_cb(self): #remove song from browser
        pos = mp3player.brow.value() #song index number
        mp3player.mediaList.remove_index(pos-1) #remove from media list
        mp3player.musicPlayer.set_media_list(mp3player.mediaList) #set new media list to music player
        mp3player.brow.remove(pos) #remove from browser
        

    def loop_cb(self): #repeat the song indefinitely 
        mp3player.looping = not mp3player.looping #opposite of last selection
        if mp3player.looping == True: 
            mp3player.musicPlayer.set_playback_mode(vlc.PlaybackMode.repeat) #loop one song
        else:
            mp3player.musicPlayer.set_playback_mode(vlc.PlaybackMode.loop) #loop playlist
            
    def vol_cb(self): #set volume from slider
        mp3player.musicPlayer.get_media_player().audio_set_volume(int(mp3player.vol.value())) #get media player instance then set value from 0-100 
    
    mb = Fl_Menu_Bar(0,0, 700 ,30)
    mb.add("File/Open",ord('o'), addSongs) #menu item to add songs
    mb.add("File/Clear",FL_BackSpace, clearSongs) #menu item to clear songs
    win.end()
    
    #callbacks for buttons
    backbut.callback(move_cb, -1)
    playbut.callback(play_cb)
    forbut.callback(move_cb, 1)
    stopbut.callback(stop_cb)
    rembut.callback(rem_cb)
    loopbut.callback(loop_cb)
    brow.callback(brow_cb)
    vol.callback(vol_cb)
    win.resizable(win)
    
    #shortcuts 
    backbut.shortcut(FL_Up)
    playbut.shortcut(FL_Enter)
    forbut.shortcut(FL_Down)
    stopbut.shortcut(FL_Shift_L | FL_Enter)
    rembut.shortcut(FL_Delete)
    loopbut.shortcut(ord('r'))
    
    #tooltips
    backbut.tooltip("Play next song (Up Arrow)")
    playbut.tooltip("Play selected song (Enter)")
    forbut.tooltip("Play previous song (Down Arrow)")
    stopbut.tooltip("Pause the current song (Left Shift and Enter")
    rembut.tooltip("Remove selected song from the browser (Delete)")
    loopbut.tooltip("Repeat the song (R)")
    vol.tooltip("Volume Slider")
    out.tooltip("Selected song")
    brow.tooltip("Select song to play")

    win.show()
    

mp3 = mp3player()
Fl.run()

