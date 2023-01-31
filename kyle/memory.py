#!/usr/bin/python
from fltk import *
import random
import os,io
from PIL import Image

def show(w):
    i=buttons.index(w)
    if i in I: 
        #do nothing if same button. 
        return
 
    I.append(i)
    w.image(imgs[i]) #show image
    w.redraw()
      
    #check if same image
    if len(I)==2:
        if fnames[I[0]]==fnames[I[1]]:
            buttons[I[0]].deactivate()
            buttons[I[0]].image().inactive()
            buttons[I[1]].deactivate()
            buttons[I[1]].image().inactive()
            I.clear()
    elif len(I)==3:
        buttons[I[1]].image(marvel)
        buttons[I[1]].redraw()
        buttons[I[0]].image(marvel)
        buttons[I[0]].redraw()
        I.pop(1)
        I.pop(0)#order matters. Must remove in reverse order
    
    #check if win
    win=True
    for but in buttons:
          if but.active():
                win=False
                break
    if win:
        fl_message('You Win!')

def png_resiz_fltk(fname,w,h):
    '''resizes png file and returns Fl_PNG_Image object. Requires importing io and PIL Image '''
    img = Image.open(fname)
    #img = img.resize((w,h),Image.LANCZOS) #LANCZOS is highest quality filter
    img = img.resize((w,h),Image.BICUBIC) #BICUBIC is good quality filter
    #img = img.resize((w,h)) # default resample filter is bicubic (good quality) in later version of PIL
    temp = io.BytesIO()  # temp is an in memory file object byte stream
    img.save(temp,'PNG') # PIL Image.save img to png format file object temp
    siz = temp.tell()    # number of bytes in image (clever way to get size without reading again)
    #next line is Fl_PNG_Image ctor overloaded for in memory objects. It works in pyfltk!!!! :)
    return Fl_PNG_Image(None, temp.getvalue(), siz) #io.BytesIO .getvalue() converts contents to bytes


I=[]
fnames=os.listdir('marvel_pics')
fnames=fnames+fnames
random.shuffle(fnames)
imgs=[]
for fname in fnames:
    imgs.append(png_resiz_fltk(f'./marvel_pics/{fname}',150,150))
    #imgs.append(Fl_PNG_Image(f'./marvel_pics/{fname}').copy(150,150))
buttons=[]
x=0
win=Fl_Window(900,600,'pyFLTK Memory')
win.begin()
for r in range(4):
    for c in range(6):
        but=Fl_Button(c*150,r*150,150,150)
        but.color(FL_BACKGROUND2_COLOR)
        marvel=png_resiz_fltk('marvel.png',150,150)
        but.image(marvel)
        but.clear_visible_focus()
        but.callback(show)
        x+=1
        buttons.append(but)
win.resizable(win)
win.end()
win.show()
Fl.run()


