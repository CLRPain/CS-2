#!/usr/bin/python
from fltk import *
from random import shuffle
from os import listdir
from io import BytesIO
from PIL import Image

def png_resiz_fltk(fname,w,h):
    '''resizes png file and returns Fl_PNG_Image object. Requires importing io and PIL Image '''
    img = Image.open(fname)
    #img = img.resize((w,h),Image.LANCZOS) #LANCZOS is highest quality filter
    img = img.resize((w,h),Image.BICUBIC) #BICUBIC is good quality filter
    #img = img.resize((w,h)) 
    # default resample filter is bicubic (good quality) in later version of PIL
    temp = BytesIO()  # temp is an in memory file object byte stream
    img.save(temp,'PNG') # PIL Image.save img to png format file object temp
    siz = temp.tell()    
    # number of bytes in image (clever way to get size without reading again)
    #next line is Fl_PNG_Image ctor overloaded for in memory objects. 
    #It works in pyfltk!!!! :)
    return Fl_PNG_Image(None, temp.getvalue(), siz) 
    #io.BytesIO .getvalue() converts contents to bytes
    
class memory(Fl_Window):
    def __init__(self, w, h, label):
        Fl_Window.__init__(self, w, h, label)
        fnames = listdir('marvel_pics') #names/shuffle
        self.fnames = fnames*2
        shuffle(self.fnames)
        self.I = []
        self.imgs = [] #image list fnames is names
        x = 0
        self.buttons = []
        for fname in self.fnames:
            self.imgs.append(png_resiz_fltk(f'./marvel_pics/{fname}',150,150))

        self.begin()
        for row in range(4):
            for col in range(6):
                but = Fl_Button(col*150,row*150,150,150)
                but.color(FL_BACKGROUND2_COLOR)
                self.marvel = png_resiz_fltk('marvel.png',150,150)
                but.image(self.marvel)
                but.clear_visible_focus()
                but.callback(self.showimg)
                x += 1
                self.buttons.append(but)
        self.resizable(self) #e
        self.end() #e

    def showimg(self, w):
        i = self.buttons.index(w)
        if i in self.I: 
            #do nothing if same button. 
            return
    
        self.I.append(i)
        w.image(self.imgs[i]) #show image
        w.redraw()
        
        #check if same image
        if len(self.I) == 2:
            if self.fnames[self.I[0]] == self.fnames[self.I[1]]:
                self.buttons[self.I[0]].deactivate()
                self.buttons[self.I[0]].image().inactive()
                self.buttons[self.I[1]].deactivate()
                self.buttons[self.I[1]].image().inactive()
                self.I.clear()
        elif len(self.I) == 3:
            self.buttons[self.I[1]].image(self.marvel)
            self.buttons[self.I[1]].redraw()
            self.buttons[self.I[0]].image(self.marvel)
            self.buttons[self.I[0]].redraw()
            self.I.pop(1)
            self.I.pop(0)#order matters. Must remove in reverse order
        
        #check if win
        win = True
        for but in self.buttons:
            if but.active():
                    win = False
                    break
        if win:
            fl_message('You Win!')
        
        
if __name__ == '__main__':
    memory = memory(900, 600, "memory")
    memory.show()
    Fl.run()






















