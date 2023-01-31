from fltk import *
import os

def next_cb(wid,n):
    global x
    if Fl.event_button() == FL_MIDDLE_MOUSE:
        files.clear() #files=[] creates local variable
        files.extend(get_filenames())
    x=x+n # n is +1 for right -1 for left
    if len(files)==0:
        fl_alert('No photos in directory')
        return
    fname=files[x%len(files)]
    if fname[-4:]=='.png':
        img=Fl_PNG_Image(fname)
    else:
        img=Fl_JPEG_Image(fname)
    ar=img.w()/img.h()
    h=int(pw/ar)
    win.resize(win.x(),win.y(),ww,h)
    picbox.image(img.copy(pw,h))
    picbox.redraw()

def get_filenames():
    d=fl_dir_chooser('Pick a directory to view photos','')
    if d==None: # Cancel clicked
        return []
    fnames=os.listdir(d)
    picnames=[]
    for name in fnames:
        if name[-4:] in ('.png','.jpg','jpeg'):
            picnames.append(os.path.join(d,name))
    return picnames

x=-1
files=get_filenames()
pw=700 #pic width
bw=50  #button width
ww=pw+(2*bw) #window width
wh=300 #arbitrary value

win=Fl_Window(0,0,ww,wh,'pyFltk Imageviewer')
win.begin()

lbut=Fl_Button(0,0,bw,wh,'@<')
lbut.callback(next_cb,-1)
lbut.tooltip('Middle click to select new directory')
lbut.shortcut(FL_ALT|FL_Left)

picbox=Fl_Box(bw,0,pw,wh)

rbut=Fl_Button(bw+pw,0,bw,wh,'@>')
rbut.callback(next_cb,1)
rbut.tooltip('Middle click to select new directory')
rbut.shortcut(FL_ALT|FL_Right)

win.end()
win.resizable(picbox)
Fl.scheme('plastic')
win.show()
Fl.run()


