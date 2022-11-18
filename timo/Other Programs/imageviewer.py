from fltk import *
import os

class mybutton(Fl_Button):
    def __init__(self, x, y, w, h, label=None):
        Fl_Button.__init__(self ,x , y, w, h, label)

    def handle(self, event):
        retval = super().handle(event)
        #must call base class handle method for event
        if event == FL_ENTER:
            self.color(FL_BLUE)
            self.redraw()
            return 1
        elif event == FL_LEAVE:
            self.color(FL_BACKGROUND_COLOR)
            self.redraw()
            return 1
        else:
            return retval 
            #return base class retval if we did not handle it


class mybox(Fl_Box):
    def __init__(self, x, y, w, h):
        Fl_Box.__init__(self, x,y,w,h)
        self.pic=None

    def setimage(self, img):
        self.pic=img    #store original image
        self.image(img) #display image
        self.redraw()   #marks widget as needing to have draw method called

    def draw(self):
        super().draw()
        if self.pic!=None:
            self.image(self.pic.copy( self.w(), self.h()))
            #notice .copy (resize) always modifies the original image


class imgviewer(Fl_Window):
    def __init__(self,  x=0, y=0, pw=700, bw=50):
        self.pw=pw #need self for next_cb method
        self.ind=-1
        self.files=self.get_filenames()
        self.ww=pw+(2*bw) #window width
        wh=300 #arbitrary value

        Fl_Window.__init__(self, x, y, self.ww, wh,'pyFltk Imageviewer')
        self.begin()

        self.lbut=mybutton(0,0,bw,wh,'@<')
        self.lbut.callback(self.next_cb,-1)
        self.lbut.tooltip('Middle click to select new directory')
        self.lbut.shortcut(FL_ALT|FL_Left)

        self.picbox=mybox(bw,0,pw,wh)

        self.rbut=mybutton(bw+pw,0,bw,wh,'@>')
        self.rbut.callback(self.next_cb,1)
        self.rbut.tooltip('Middle click to select new directory')
        self.rbut.shortcut(FL_ALT|FL_Right)

        self.end()
        self.resizable(self.picbox)

    def next_cb(self,wid,n):
        if Fl.event_button() == FL_MIDDLE_MOUSE:
            self.files=[] #with self. can now use =[] instead of .clear()
            self.files.extend(self.get_filenames())
        self.ind = self.ind + n # n is +1 for right -1 for left
        if len(self.files)==0:
            fl_alert('No photos in directory')
            return
        fname=self.files[self.ind%len(self.files)]
        if fname[-4:]=='.png':
            img=Fl_PNG_Image(fname)
        else:
            img=Fl_JPEG_Image(fname)
        ar=img.w()/img.h()
        h=int(self.pw/ar)
        self.size(self.ww,h) #resizing window causes picbox to also resize
        #self.picbox.image(img.copy(self.pw,h))
        #self.picbox.redraw() #use setimage from mybox class instead
        self.picbox.setimage(img)

    def get_filenames(self):
        #notice variables in this function do not require self.
        #because nothing is required to be persistant in the class
        d=fl_dir_chooser('Pick a directory to view photos','')
        if d==None: # Cancel clicked
            return []
        fnames=os.listdir(d)
        picnames=[]
        for name in fnames:
            if name[-4:] in ('.png','.jpg','jpeg'):
                picnames.append(os.path.join(d,name))
        return picnames

if __name__=='__main__':
    Fl.scheme('plastic')
    app=imgviewer()
    app.show()
    Fl.run()
